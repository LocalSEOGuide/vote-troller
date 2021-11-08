import selinium
import selinium-wire

# provide targets
list_of_names = ['Rejoice Ojiaku', 'Wilhemina Davis', 'Aimee Sanford', 'Rachel Anderson', 'Alison Enzinna',
                 'Bria Poullard', 'Caleb Romo', 'Jess Peck', 'Bryan Heckler', 'Tessa Voecks']

# provide element/attribute (text) to find + element/attribute to click
target_elements = {'root_ele':  {
    'class': 'seo_expert-item'
},
    'click_target': {
        'onclick':'LikeBtn.vote'
    }
}


Class VoteTroller:
    def __init__(self):
        print('Testing')

