HEROKU = False # Make it False if you're not deploying on heroku.

if HEROKU:
    from os import environ

    bot_token = environ["bot_token"]
    ARQ_API_KEY = environ["ARQ_API_KEY"]
    LANGUAGE = environ["LANGUAGE"]

# NOTE Fill this if you are not deploying on heroku.
if not HEROKU:

    bot_token = "6226805699:AAE1T96RKSjs06kNID7VW9xVsYaSOFDI92o"
    api_id2=13958802
    api_hash2="f6d2d3b04309e9660a0be5b2a6195a7c"
    session_string="BQDU_pIAXoKacHY7FmwGEWTozwOEjLbdZqf_c2yYKGElslXEdnmDkcs7VE4-hUiwfXGlmVWRroKat2PPVuj-oT8Fj9pSTOaKPTdDH9lxIOLukYsAnLqjafv9RPduahpX7b8aeXdR71d_1kNwxIy39l874vZz8jFZIi6R_kgp_qacX7s_pF-4eGQDszfmIR6flqXRNls4-DAsgJzRtIC1HlF96rPWQBA-V38e9OUd9yXRHP24pnGadzNDV3PC9s24wRowxctuV3ZWnWQfuBpiCfb1jBsvmWd6j3snbPxsjuYM_0KH9MbYWVUnszOce3Nm7jTksEMMhbMsejtZBrQGkVGCVs3bJAAAAAF3J43eAA"
    ARQ_API_KEY = "KGPAJO-NJFKTD-TICNMP-YWEOEZ-ARQ" #"QKILRQ-VUTFDL-MQBWZA-EGQFPM-ARQ" #"LCZFSR-XCJSNJ-JVHHXC-UUVLWE-ARQ"
# List of supported languages >>
# https://py-googletrans.readthedocs.io/en/latest/#googletrans-languages
    LANGUAGE = "vi"

# Leave it as it is
ARQ_API_BASE_URL = "https://arq.hamker.dev"
