import base64
import os
from datetime import datetime
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import EmotionImage

@csrf_exempt
def upload_image(request):
    import json
    if request.method == 'POST':
        data = json.loads(request.body)
        image_data = data.get('image')
        emotion = data.get('emotion')

        if not image_data or not emotion:
            return JsonResponse({'status': 'error', 'message': 'Rasm yoki emotion yoq'})

        format, imgstr = image_data.split(';base64,') 
        image_bytes = base64.b64decode(imgstr)

        folder = 'media/face_images'
        os.makedirs(folder, exist_ok=True)
        filename = f"{emotion}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
        filepath = os.path.join(folder, filename)

        with open(filepath, 'wb') as f:
            f.write(image_bytes)

        EmotionImage.objects.create(
            image=f"face_images/{filename}",
            emotion=emotion
        )

        return JsonResponse({'status': 'success', 'filename': filename})
    return JsonResponse({"status': 'error', 'message': 'POST bo'lishi kerak"})

def camera_view(request):
    return render(request, 'camera.html')
