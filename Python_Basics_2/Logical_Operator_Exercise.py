# Logical Operator Exercise
is_magician = False
is_expert = False

# check if magician and expert: " you are a master magician "
if is_magician and is_expert:
    print("you are a master magician")
# check if magician but not expert "at least you're getting there"
elif is_magician and not is_expert:
    print("at least you're getting there")
# if you aren't a magician "You need magic"
elif not is_magician:
    print("You need magic")
