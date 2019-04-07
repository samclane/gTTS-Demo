import os
import uuid

from django.http import HttpResponse
from django.shortcuts import render
from gtts import gTTS

from gettingstarted.settings import BASE_DIR

if os.name != 'nt':
    BASE_DIR = "/tmp"
else:
    BASE_DIR += "\\audio"


# Create your views here.
def index(request):
    if request.method == 'POST':
        uid = uuid.uuid4()
        filename = r"file_{}.mp3".format(uid)
        phrase = request.POST.get('textfield', None)
        try:
            tts = gTTS(phrase, lang='en')
            with open(os.path.join(BASE_DIR, filename), 'wb') as f:
                tts.write_to_fp(f)
            return render(request, "index.html", {"link": os.path.join(BASE_DIR, filename),
                                                  "phrase": phrase})
        except Exception as exc:
            return HttpResponse(f"Exception thrown during speak attempt: {exc}\n")
    else:
        return render(request, "index.html")
