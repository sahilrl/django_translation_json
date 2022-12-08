from django.utils.encoding import force_str

def build_localized_fieldname(field_name, lang):
    if lang == 'id':
        # The 2-letter Indonesian language code is problematic with the
        # current naming scheme as Django foreign keys also add "id" suffix.
        lang = 'ind'
    return str('%s_%s' % (field_name, lang.replace('-', '_')))


def build_localized_verbose_name(verbose_name, lang):
    if lang == 'id':
        lang = 'ind'
    return force_str('%s [%s]') % (force_str(verbose_name), lang)