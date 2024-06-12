HEROKU = False # Make it False if you're not deploying on heroku.

if HEROKU:
    from os import environ

    bot_token = environ["bot_token"]
    ARQ_API_KEY = environ["ARQ_API_KEY"]
    LANGUAGE = environ["LANGUAGE"]

# NOTE Fill this if you are not deploying on heroku.
if not HEROKU:

    bot_token = "6543379161:AAFRJFLuItZt-Ds_CdLVUcQU5tT0d7f4Yk0"
    api_id2=29966047
    api_hash2="218e27785e7f07bce53559386e2eb87a"
    session_string="BQHJPt8AiYC8KohjPXSYLCnMGu1Fz46wDsW3Ye3cPxldlP3MO30uKaAjsHO1cLJbiqlJyg6IlxDjeCpsdzIzWxcrK8NZwJW7xnHFxLN61RziI0eoBdof7wT05vH1fGzuuz3lmTsSdJRDqXD9_e603mn7WZUMHzDJw9-EyjUOIqq77djYCFHvRJvNTPOPJ_DcZCB8Gm7rVNHYIdQ92unXVQ3w21y4u-0WN5ApCcWIy1_RY7WkRE7WCXYeYEhLmJ4Lnd9Hl9hOnhwp93vHMo97BRTO0XQqtymFjD8hvuDcQ9tZ9XHhNw2x2UPu5awH-qnvRQMHcQAiisy6gauJvefM0T0VGWtlYQAAAAF_g_wRAA"
    ARQ_API_KEY = "KGPAJO-NJFKTD-TICNMP-YWEOEZ-ARQ" #"QKILRQ-VUTFDL-MQBWZA-EGQFPM-ARQ" #"LCZFSR-XCJSNJ-JVHHXC-UUVLWE-ARQ"
# List of supported languages >>
# https://py-googletrans.readthedocs.io/en/latest/#googletrans-languages
    LANGUAGE = "vi"

# Leave it as it is
ARQ_API_BASE_URL = "https://arq.hamker.dev"
