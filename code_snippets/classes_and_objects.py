class ClassName:
    def display_name(self):
        print('display_name')

    def display_(_self):
        print('display_')

    def _name(_self):
        print('name')

cn = ClassName()
cn.display_()
cn.display_()
cn.display_name()
cn.display_name()
cn._name()

print('-----------')
new_obj = ClassName()
new_obj.display_name()
