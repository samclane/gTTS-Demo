from django.http import HttpResponse
from django.shortcuts import render
from gettingstarted.settings import BASE_DIR
import os

from gtts import gTTS


# Create your views here.
def index(request):
    if request.method == 'POST':
        phrase = request.POST.get('textfield', None)
        try:
            tts = gTTS(phrase, lang='en')
            with open(os.path.join('/tmp/', r"file.mp3"), 'wb') as f:
                tts.write_to_fp(f)
            return render(request, "index.html", {"link": os.path.join('/tmp/', r"file.mp3")})
        except Exception as exc:
            return HttpResponse(f"Exception thrown during speak attempt: {exc}\n")
    else:
        return render(request, "index.html")

