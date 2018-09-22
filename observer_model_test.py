#! python3
# Observer Model trial/example


# Create an observable object which will contain information of varying types
class Publisher():
    def __init__(self):
        # Some 'single value' variables, these are indpendent variables that
        # we desire to put on a single list but update independently - meaning
        # we don't want to create multiple lists (I.e. one for each variable to be
        # monitored).
        self._file_name = ''
        self._dir_name = ''
        self._some_value = ''

        # Some 'multiple value' variables; as with the 'single value'
        # variables, we want to keep all subscribers on a single list
        # yet update them all independently
        self._num_list = []
        self._word_list = []

        # The subscriber lists, one for variables that only expect a 'single'
        # value and one for a list of variables that expect a array/list/tuple
        self._subs_single = []
        self._subs_mult = []

    def set_file_name(self, new_name):
        self._file_name = new_name
        self.update_subs('file', self._file_name)

    def set_dir_name(self, new_dir):
        self._dir_name = new_dir

    def set_some_value(self, new_val):
        self._some_value = new_val

    def set_num_list(self, new_nums):
        try:
            for item in new_nums:
                self._num_list.append(item)
        except TypeError:
            self._num_list.append(new_nums)

    def set_word_list(self, new_words):
        try:
            for item in new_words:
                self._word_list.append(item)
        except TypeError:
            self._word_list.append(new_words)

    def add_sub(self, sub, single=True):
        if single is True:
            self._subs_single.append(sub)
        else:
            self._subs_mult.append(sub)

    def get_subs(self):
        print('Single var subs: {}'.format(self._subs_single))
        print('Array subs: {}'.format(self._subs_mult))

    def update_subs(self, subject, var, single=True):
        # subject = keyword that must be found in the variable-to-be-updated's
        # name.  For example, if we were to be updating a subscriber to
        # 'self._file_name' we might use 'file' as the subject and therefore,
        # the variable-to-be-updated's name should include the string 'file'
        # var = the variable that has the value the subscribers want
        # single=True = This is simply a default action to prevent from having
        # to designate which list to use EVERY time - now, only some times
        if single is True:
            for sub in self._subs_single:
                name = sub.get_name()
                if name.find(subject) != -1:
                    sub.update(var)
        else:
            for sub in self._subs_mult:
                if sub.find(subject) != -1:
                    sub.update(var)


class Watcher():
    def __init__(self, name):
        self._my_value = ''
        self._name = name

    def get_name(self):
        return self._name

    def get_val(self):
        return self._my_value

    def update(self, val):
        self._my_value = val
        print('[+] New value assigned: {}'.format(self._my_value))


pub = Publisher()

file_watcher1 = Watcher('file_watcher1')
pub.add_sub(file_watcher1)

pub.get_subs()

pub.set_file_name('python.py')
print(file_watcher1.get_val())










