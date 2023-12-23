HEROKU = False # Make it False if you're not deploying on heroku.

if HEROKU:
    from os import environ

    bot_token = environ["bot_token"]
    ARQ_API_KEY = environ["ARQ_API_KEY"]
    LANGUAGE = environ["LANGUAGE"]

# NOTE Fill this if you are not deploying on heroku.
if not HEROKU:

    bot_token = "6226805699:AAE1T96RKSjs06kNID7VW9xVsYaSOFDI92o"
    api_id2=24449619
    api_hash2="70bab6764c1e34eae004925f8ec0e122"
    session_string="BQF1ElMAmYJyE8YVm-k41BNYrdTjPHGrR3r6yXOI2ly6FirqWNJPtxPXkXoQ0BcrATqe8n6FvLo8tw4wQkUE_bUfYP9QA5k25CsVNqFlX1zs4QWdgjyCu_9gYxAMroaYWkbJJrcS9JpmOFnz5fHD9gUyCU3OK4n0tEOSmcLmkNw3Tt7f7wMr6f5Jt6YJAKI6jHyPeZLZv8dvRpl8cMhTt5nt_adknorYB5jH2QKnEV7utW9QNtQNDPTCo98QREXuoQcIHSUX7DdtKzhZDzWA1j1oxQRZ7-9tL3gjY2f2kkO45qKxmwAR4yKs5tLBO4Q3jSagWMZhCZ4x95E5VIe0aZY0hD5gKgAAAAGI5tIhAA"
    ARQ_API_KEY = "QKILRQ-VUTFDL-MQBWZA-EGQFPM-ARQ" #"LCZFSR-XCJSNJ-JVHHXC-UUVLWE-ARQ"
# List of supported languages >>
# https://py-googletrans.readthedocs.io/en/latest/#googletrans-languages
    LANGUAGE = "vi"

# Leave it as it is
ARQ_API_BASE_URL = "https://arq.hamker.dev"
