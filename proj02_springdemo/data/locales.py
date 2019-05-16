import json
import os

All_Locales = ["en_AP", "en_AU", "nl_BE", "fr_BE", "pt_BR", "en_CA", "fr_CA", "cs_CZ", "zh_CN", "da_DK", "de_DE", "es_ES", "en_EU", "fr_FR", "el_GR", "en_GU", "en_IN", "id_ID", "en_IE", "it_IT", "ko_KR", "es_XX", "fr_LU", "hu_HU", "es_MX", "en_ZZ", "nl_NL", "no_NO", "de_AT", "pl_PL", "pt_PT", "de_CH", "en_AA", "fr_CH", "fi_FI", "sv_SE", "it_CH", "th_TH", "tr_TR", "en_GB", "vi_VN", "ru_RU", "zh_TW"]

Closing = ["en_IN", "th_TH", "ko_KR", "vi_VN", "en_GU", "en_ZZ", "pt_BR", "id_ID", "en_AP", "es_MX", "en_GB", "en_IE", "fr_FR", "en_AA", "el_GR", "es_ES", "pt_PT", "it_IT", "en_AU", "en_EU", "hu_HU", "cs_CZ", "pl_PL"]

Online = ["es_XX", "zh_TW", "en_CA", "fr_CA", "de_AT", "de_DE", "fr_CH", "it_CH", "de_CH", "fr_BE", "nl_BE", "fr_LU", "nl_NL", "no_NO", "sv_SE", "da_DK", "fi_FI"]

Special = ["zh_CN", "ru_RU", "tr_TR"]