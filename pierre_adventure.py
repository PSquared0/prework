name = raw_input("Type in the name of the average joe in this story: ")
hero = raw_input("Name the superheroine or hero?: ")
power = raw_input("Name a super power?: ") 

print "\n"
print "One day %s was walking down the street and heard someone calling for help." % (name)
print "%s ran toward the cries as fast as possible to a unusually unsupervised chemical plant." % (name)
print "There was a young boy hanging over the edge of a platform about to fall into a vat of green ooze! (Someone is getting sued, who is in charge here?)"
print "%s runs toward the boy to save him and arrives at the same time as the incredible, awesome, splediferous %s!" % (name, hero)
print "\n" 
print "If you want %s to save the boy, choose '1'" % (name)
print "if you want %s to save the boy choose '2'" % (hero)

activity = int(raw_input("Who saves the young boy?: "))

if activity == 1:
    print "\n"
    print "A good samaritan like %s doesn't hesitate and runs across the platform toward the boy." % (name)
    print "%s grabs the boys flailing hand and pulls with all their might." % (name)
    print "The boy begins to slip but before he does, %s give one last heroic heave and pulls the boy to safety." % (name)
    print "....Only to lose thier own balance on the other side of the platform and falls direclty into the purtrid green bath of ooze!"
    print "\n"
    print "%s jumps in after %s (what were they doing this whole time, Instagramming??) and pulls %s to safety." % (hero, name, name)
    print "'Are you allright?' says %s. %s, looking bewildered says, 'Yes, I think I am, I, I think im going to go home now, I dont have insurance.'" % (hero, name)
    print "\n"
    print "%s walks home, marveling at the recent brave deed, but starts to feel weird." % (name)
    print "\n"
    print "6 months later...."
    print "\n"
    print "%s stands on a rooftop surveying their city, hidden in the shadows looking for prey." % (name)
    print "That fateful day six months ago was the birth of %sperson! Imbued with the power of %s!" % (power, power)

    print "%sperson is : (pick a number) " % (power)
    print "\n"
    print '1. "A Good Guy"'
    print '2. "A Villan"'
    print '3. "Delusional about having super powers"'

    status = int(raw_input(">"))
    if status == 1:
            print "From this high vantage point stands,"
            print "%sperson, the most mediocre crimefighter in the in city's history." % (power)
            print "They have about a 25 percent success rate and 6 months from now falls in a vat of pink ooze trying to save a goldfish and loses their power of %s" % (power)

    elif status == 2: 
            print "From this high vantage point stands,"
            print "%sperson, the most feared villan in the city's history." % (power)
            print "They rule the city with an iron fist and dies at a ripe old age of 103 surrounded by loved ones"

    elif status == 3:
            print "From this high vantage point stands %s, who sees someone in need and leaps to action..." % (name)
            print "and promptly falls off the roof on which they were perching. All the while yelling 'I am %sperson' over and over." % (power)

    else:
        print "Um, why did you press that? That wasn't a 1,2 OR 3"
        print "Start again by running 'python pierre_adventure.py when you have learned how to count'"

elif activity == 2:
    print "\n"
    print "%s is here to save the day!" % (hero)
    print "%s shoves %s out of the way and leaps to the boys side" % (hero, name)
    print "%s watches helplessly as the courageous dogooder picks the boy up with ease and carries him to safety" % (name)
    print "%s observes the hero departing and now bored (how anti-climatic was that?) decides to: (pick a number)" % (name)
    print "\n"
    print '1. "Dip a toe in the ooze to try and manifest super powers"'
    print '2. "Pretend to fall into the vat. That unnamed hero looked pretty cute under that mask, maybe %s can get a date or at least a number"' % (name)
    print '3. "Share this experince on social media, how did they not Persicope the save then they had the chance. %s"s followers would have loved it!"' % (name)
    print "\n"

    lame = int(raw_input(">"))
    print "\n"
    if lame == 1:
        print "%s walks up to the edge of the platform, mesmerized by the lull of the ooze." % (name)
        print "'I've always wanted super powers', %s says" % (name)
        print "What could go wrong?"

        print "\n"
        print "1 week later..."

        print "\n"
        print "%s is imbued with the power of %s and is a hero to the world!" % (name, power)
        print "just kidding, %s actually became Patient Zero for zombism that, in turn, devestates the world. The fast kind, like 28 Days Later style" % (name)
        print "Thanks a lot %s" % (name)
        print "The End"


    elif lame == 2:
        print "%s walks over to the bubbling cauldron of green stuff." % (name)
        print "Oh my, I am super woozy from these fumes, %s proclaims loudly, I oh so hope I do not fall in" % (name)
        print "Whoooaaaaa, here I goooooo, unless someone cute comes and saves meeeee! %s says before falling into the vat of gross ickyness" % (name)
        print "\n"
        print "35 years later..."
        print "\n"
        print "Medical students crowd around a hospital bed along with the instructing doctor."
        print "'And here', the doctor says, 'lies our most famous patient'"
        print "This person ahs been in a coma for almost 30 years with no sign of trauma."
        print "The only thing we an observe is that the patient constantly floats 1 foot over their bed"
        print "And most interestingly whenever an attractive person walks by the patient starts to %s" % (power)
        print "The End"

    elif lame == 3:
        print "'well if I missed the action I can at least Instagramm the ooze', %s thinks aloud." % (name)
        print "%s leans over to get a good shot....and promtly drops their phone in the vat of putrid putridness"
        print "Fin"
    
    else:
        print "Um, why did you press that? That wasn't a 1,2 OR a 3"
        print "Start again by running 'python pierre_adventure.py when you have learned how to count'"





