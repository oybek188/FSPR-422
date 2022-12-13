def get_user_info(name, clan='Trident', *args, **kwargs):
    if args:
        args = "".join([f"\n- {arg}" for arg in args])
        return f"Your name is {name} and your clan is {clan}. Other information:{args}"
    else:
        return f"Your name is {name} and your clan is {clan}."
    
print(get_user_info("Behruz"))
print(get_user_info("Behruz", "Shunko"))
print(get_user_info("Behruz", "Shunko", 'sonic speed', 'lightning', 'programming'))
print(get_user_info("Behruz", "Shunko", 'sonic speed', 'lightning', 'programming', db="SQL"))
    