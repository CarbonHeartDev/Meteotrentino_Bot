from .file_url_helper import name_from_url, file_exists, relative_to_absolute
import urllib

def get_miniature(webUrl):
    retval=relative_to_absolute("\\Data\\img_cache\\icons\\")+name_from_url(webUrl)
    if not(file_exists(retval)):
        f = open(retval,'wb')
        f.write(urllib.request.urlopen(webUrl).read())
        f.close()
    return retval


