class Lame:
    def __init__(self):
        self.name = 'lame name'

new_lame = Lame()
print(new_lame)
# will return the same as print does,
# because print returns stringified version of an object
print(str(new_lame))
print()

class Not_Lame:
    def __init__(self) -> None:
        self.name = 'Not so lame now'

    def __str__(self) -> str:
        return self.name
    
new_not_lame = Not_Lame()
# will return self.name as it is the custom stringified representation of the class
print(new_not_lame)
# will return the same as print, again
print(str(new_not_lame))
print()

# len works the same way, custom class won't have it by default
# print(len(new_not_lame))

class Ruler:
    def __init__(self, max_length) -> None:
        self.max_length = max_length

    def __len__(self):
        return self.max_length
    
new_ruler = Ruler(100)
# class' custom method for len will be called here
print(len(new_ruler))
print()

# del removes an  object from the memory
del new_not_lame
# print(new_not_lame)

# del can also be configured as a special method
class Deletable:
    def __init__(self, instance_number) -> None:
        self.deletable = True
        self.instance_number = instance_number

    def __del__(self):
        print(f'WARNING!! Deletable instance #{self.instance_number} will be purged')

new_deletable = Deletable(4)
print(new_deletable.instance_number)
# will print warning in console
del new_deletable
print(new_deletable)