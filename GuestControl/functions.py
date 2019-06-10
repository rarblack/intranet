def base64_to_content_file(base64_string, username, datetime):
    from django.core.files.base import ContentFile
    import base64
    format, imgstr = base64_string.split(';base64,')
    ext = format.split('/')[-1]
    name = f'{username}_{datetime}.{ext}'
    data = ContentFile(base64.b64decode(imgstr), name=name)
    return data, name