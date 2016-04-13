def modified_field(bool_field, modifier_field, ammount):
    if bool_field:
        return modifier_field + ammount
    else:
        return modifier_field
