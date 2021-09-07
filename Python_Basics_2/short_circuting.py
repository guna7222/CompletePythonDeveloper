# Short Circuiting
# and or are short circuits
is_have_facebook_account = True
is_have_whatsapp_account = False

if is_have_whatsapp_account or is_have_facebook_account:
    print('Using Social Media Account')
else:
    print('not using social media account')