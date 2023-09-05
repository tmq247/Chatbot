HEROKU = False # Make it False if you're not deploying on heroku.

if HEROKU:
    from os import environ

    bot_token = environ["bot_token"]
    ARQ_API_KEY = environ["ARQ_API_KEY"]
    LANGUAGE = environ["LANGUAGE"]

# NOTE Fill this if you are not deploying on heroku.
if not HEROKU:

    bot_token = "6201708385:AAERAJJ5BYkPgGXKogdqgpKkNWyY21O3lhs"
    ARQ_API_KEY = "LCZFSR-XCJSNJ-JVHHXC-UUVLWE-ARQ"
# List of supported languages >>
# https://py-googletrans.readthedocs.io/en/latest/#googletrans-languages
    LANGUAGE = "vi"

# Leave it as it is
ARQ_API_BASE_URL = "https://arq.hamker.dev"
