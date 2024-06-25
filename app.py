from flask import Flask, render_template, request, send_file
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
import nltk
import PyPDF2
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

nltk.download('punkt')

app = Flask(__name__)



def count_words(text):
    return len(text.split())

def summarize_text(text, sentences_count):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    stemmer = Stemmer("english")
    summarizer = LsaSummarizer(stemmer)
    summarizer.stop_words = get_stop_words("english")
    
    summary = summarizer(parser.document, sentences_count)
    summary_text = " ".join([str(sentence) for sentence in summary])
    return summary_text

def read_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def create_pdf(article, summary, summary_type, article_word_count, summary_word_count):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()
    
    story = []
    story.append(Paragraph("Original Article", styles['Heading1']))
    story.append(Paragraph(f"Word count: {article_word_count}", styles['Normal']))
    story.append(Paragraph(article, styles['Normal']))
    story.append(Paragraph(f"Summary ({summary_type})", styles['Heading1']))
    story.append(Paragraph(f"Word count: {summary_word_count}", styles['Normal']))
    story.append(Paragraph(summary, styles['Normal']))
    
    doc.build(story)
    buffer.seek(0)
    return buffer

@app.route('/', methods=['GET', 'POST'])
def index():
    article = ""
    summary = ""
    summary_type = "brief"  # Default to brief summary
    article_word_count = 0
    summary_word_count = 0

    if request.method == 'POST':
        summary_type = request.form.get('summary_type', 'brief')
        
        if 'file' in request.files:
            file = request.files['file']
            if file.filename != '':
                if file.filename.endswith('.pdf'):
                    article = read_pdf(file)
                elif file.filename.endswith('.txt'):
                    article = file.read().decode('utf-8')
        else:
            article = request.form['article']
        
        if summary_type == 'brief':
            sentences_count = 3  # Adjust this for approximately 50-70 words
        else:
            sentences_count = 7  # Adjust this for approximately 150 words
        
        summary = summarize_text(article, sentences_count)
        
        article_word_count = count_words(article)
        summary_word_count = count_words(summary)

    return render_template('index.html', article=article, summary=summary, summary_type=summary_type,
                           article_word_count=article_word_count, summary_word_count=summary_word_count)




@app.route('/export-pdf', methods=['POST'])
def export_pdf():
    article = request.form['article']
    summary = request.form['summary']
    summary_type = request.form['summary_type']
    article_word_count = int(request.form['article_word_count'])
    summary_word_count = int(request.form['summary_word_count'])

    pdf_buffer = create_pdf(article, summary, summary_type, article_word_count, summary_word_count)
    
    return send_file(pdf_buffer,
                     download_name='summary.pdf',
                     as_attachment=True,
                     mimetype='application/pdf')

#if __name__ == '__main__':
 #   app.run(debug=True)