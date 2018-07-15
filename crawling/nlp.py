import re

def normalize_text(text):
    # ToDo Proper normalization
    return text.lower()\
        .replace('-', ' ') \
        .replace('_', ' ') \
        .replace('  ', ' ')

def tokenize(text):
    return re.split(r'(\d+|\W+)', text)

def check_text(text, contains, not_contains=None, normalize=True):
    if not contains:
        contains = []

    if not not_contains:
        not_contains = []

    if normalize:
        text = normalize_text(text)

    has_searched = False
    for str in contains:
        if re.search(str.lower(), text):
            has_searched = True
            break

    if not has_searched:
        return False

    has_forbidden = False
    for str in not_contains:
        if re.search(str, text):
            has_forbidden = True
            break

    return not has_forbidden

def remove_elements(text, contains):
    strName = text
    for elem in contains:
        strName=strName.replace(elem, "")
    return strName

def get_element_attribute(element):
    if element.get_attribute('id'):
        return ['id', element.get_attribute('id')]
    elif element.get_attribute('name'):
        return ['name', element.get_attribute('name')]
    elif element.get_attribute('value'):
        return ['value', element.get_attribute('value')]

    return None

def wait_until_attribute_disappear(attr_type, attr_name):
    try:
        if attr_type == "id":
            element = WebDriverWait(driver, 5).until(
                EC.invisibility_of_element_located((By.ID, attr_name))
            )
        elif attr_type == "name":
                element = WebDriverWait(driver, 5).until(
                    EC.invisibility_of_element_located((By.NAME, attr_name))
                )
    except TimeoutException:
        print('The element does not disappear')
        return False

    return True

def check_if_empty_cart(text):
    contains = ['cart is empty', 
                'no .*in .*cart',
                'zero products in .*cart', 
                'nothing in.* cart', 
                'empty cart',
                '0 items',
                'zero items'
               ]
    
    return check_text(text, contains, [])


def check_if_domain_for_sale(text, domain):
    if re.search('domain .*{}.* for sale'.format(domain), text):
        return True
    
    return False