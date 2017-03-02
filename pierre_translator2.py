eng2krey = dict()
eng2krey = {'bacon': 'la kochon', 'monster' : 'mons', 'mother' : 'monman', 'parrot' : 'jako', 'jewel':'bijou','vanilla':'vaniy', 'nice':'bon','yellow':'jon','fantastic':'kokenn','fancy':'anpenpan','darling':'cheri','concrete':'siman','fashion':'lamod','hat':'chapo'}

def trans(word):
    if word in eng2krey:
        return eng2krey[word]
        
    else:
        return "Oh no! That word doesn't exist in Kreyol!"

trans ('parrot')
