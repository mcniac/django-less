from django.conf import settings

# path to the less executable
LESS_EXECUTABLE = getattr(settings, "LESS_EXECUTABLE", "lessc")
# use cache? 
LESS_USE_CACHE = getattr(settings, "LESS_USE_CACHE", True)
# Cache timeout for inline styles (in seconds). Default: 30 days.
LESS_CACHE_TIMEOUT = getattr(settings, "LESS_CACHE_TIMEOUT", 60 * 60 * 24 * 30) # 30 days
# Cache timeout for reading the modification time of external stylesheets (in seconds). Default: 10 seconds.
LESS_MTIME_DELAY = getattr(settings, "LESS_MTIME_DELAY", 10) # 10 seconds
# Directory where we should look for the less files. defaults to STATIC_ROOT or MEDIA_ROOT
LESS_OUTPUT_DIR = getattr(settings, "LESS_OUTPUT_DIR", "LESS_CACHE")
LESS_OUTPUT_URI = getattr(settings, "LESS_OUTPUT_URI", LESS_OUTPUT_DIR)
LESS_FORCE_REGENERATE = getattr(settings, "LESS_FORCE_REGENERATE", False)
LESS_USE_URL_CONVERTER = getattr(settings, "LESS_USE_URL_CONVERTER", True)