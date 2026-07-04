from flask import Flask, render_template, request
import qrcode
import io
import base64

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    qr_image = None
    
    if request.method == 'POST':
        # Get the URL from the HTML form
        url = request.form.get('url')
        
        if url:
            # Generate the QR code
            img = qrcode.make(url)
            
            # Save the image to an in-memory bytes buffer
            img_io = io.BytesIO()
            img.save(img_io, 'PNG')
            img_io.seek(0)
            
            # Encode the image to base64 so HTML can render it directly
            qr_image = base64.b64encode(img_io.getvalue()).decode('ascii')
            
    # Pass the encoded image to the template
    return render_template('index.html', qr_image=qr_image)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)