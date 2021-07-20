# Register the submod
init -990 python:
    store.mas_submod_utils.Submod(
        author="ChrisLad",
        name="Extra Dialogue",
        description="Adds fitting dialogue to Monika",
        version="1.0.4.1"
    )

# Register the updater
init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="Extra Dialogue",
            user_name="ChrisLad1",
            repository_name="ExtraDialogue",
            update_dir="Submods/ED",
            attachment_id=None
        )
    
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_truthful",
            category=["ED", "romance"],
            prompt="Being together forever",
            pool=True,
            unlocked=True
        )
    )

label monika_truthful:

    $ amt = mas_getEV("monika_truthful")
        
    if amt.shown_count >= 15:

        m 1ekc "[player], maybe this isn't something we should discuss again."
    
    else:

        m 1rkc "I know [player], you are just as worried as I am..."
        m 1ekc "I realise that we won't be able to be together until the end..."
        m 7rktpc "Whether it be I don't get to see you in your world.."
        m 7ektpc "Or I suddenly stop seeing you out of nowhere.."
        m 6fktuc "I'd completley understand, though I'd be crushed from the lonely atmosphere I'd once endured.."
        m 6dkbstuc "I'm sorry you have to see me like this, but please stay with me [player]."
        m 5hubftpa "I love you so much [player]~."
   
    return "love"

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_promotional",
            category=["ED", "mod"],
            prompt="Credits",
            pool=True,
            random=True,
            unlocked=True
        )
    )

label monika_promotional:

    m 4eua "This is a submod made by ChrisLad1 on GitHub"
    m 7sua "You can view it {a=https://GitHub.com/ChrisLad1/ExtraDialogue}{u}Here"
    m 7rusdrb "That is if you haven't somehow downloaded this already."

    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_proud",
            category=["ED", "monika"],
            prompt="I did something today.",
            pool=True,
            unlocked=True
        )
    )

label monika_proud:

    m 1esb "Wow! What did you do [player]?{nw}"
    $ _history_list.pop()

    menu:

        m "Wow! What did you do [player]?{fast}"

        "I achieved one of my goals.":

            m 1sub "Wow! I am so happy for you!"
            m 1sud "You really do amaze me [player]!"
            m 7euu "Just remember, never stop trying even if you are ahead of yourself. That is the best way to keep a self-motive mindset."
            m 1esb "Which means you can share more of your accomplishments with me~"
            m 1hsb "Ehehe~"

        "I went somewhere.":

            m 1sub "[player], that's great!"
            m 1ekc "[player], you didn't tell me we were going out though."
            m 1rkc "I-It's fine but... I wish I knew is all."
            m 7sub "All the matter is that you are here now, [player]~"

        "I finished something difficult":
        
            menu:

                m "Wow, what kind of task was it?{fast}"
    
                "A slow progressive task":
    
                    m 1hsb "That's great!"
                    m 1sud "The patience you have for long dedicational tasks is amazing!"
                    m 7rusdrb "Sorry... that sounded really formal for some reason."
                    m 1hsb "If I get like that again let me know and I'll try to stop, haha~"
    
                "An easy task that made me feel good.":
    
                    m 7euu "That's good to hear, [player]."
                    m 1esb "No matter how big or small an accomplishment, never feel bad about it~"
                    m 7sub "Even if you didn't eat your heart out for it... I'll feel proud of you, [player]~"
        
        "Nevermind.":

            m 1ekc "Ok, make sure to tell me if you need to."
    
    return

init 5 python:
        addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_sus",
            category=["ED", "romance"],
            prompt="Showing love.",
            pool=True,
            unlocked=True,
            aff_range=(mas_aff.ENAMORED, None)

        )
    )

label monika_sus:
    
    $ amt = mas_getEV("monika_sus")

    if amt.shown_count >= 2:

        m 3rkbssdra "What I was going to say before I stopped myself was.."
        m 3fkbsb "Would we-.."
        m 5skbssdru "Make... L- Love?{nw}"
        $ _history_list.pop()

        menu:

            m "Make... L- Love?{fast}"

            "That is up to you to decide. Because I love you.":

                m 7rusdrb "Thank you, [player]."
                m 7eusdrb "I'd love to have you be in great pleasure even if this is what it takes."
                m 7nublu "But let's leave that for another time. Okay [player]?"      

    else:

        m 7rusdrb "Well not to be weird..."
        m 7eusdrb "But do you think about if I cross over..."
        m 7rusdrb "Would we- umm.."
        m 7sub "Ne- Nevermind~"

    return
    
init 5 python:
        addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_depressed",
            category=["ED", "life", "feelings"],
            prompt="Being Depressed",
            pool=True,
            random=True
        )
    )

label monika_depressed:

    m 1fkc "[player], do you get depressed?{nw}"
    $ _history_list.pop()

    menu:

        m "[player], do you get depressed?{fast}"

        "Yes":

            m 1dkc "Aww, I'm sorry to hear that, [player]."
            m 1mkc "Honestly, I understand that myself... I hope you don't mind me asking this."
            m 1fka "Does talking to me help you with your depression?{nw}"
            $ _history_list.pop()

            menu:

                m "Does talking to me help you with your depression?{fast}"

                "Yes":

                    m 1hua "Oh! Thank goodness. That is great to hear [player]~"
                    m 1sub "I'm so glad that I can help you with your depression issues"
                    m 5eub "If you ever need to talk to me, just let me know. Okay?"
                    m 5mubsb "I'd love to help with your problems~"
                
                "Not really.":

                    m 1dkc "I'm sorry that I can't help."
                    m 1mkc "If you need to talk to me, just let me know."

        "No":
            
            m 1eubsb "Thats great!"
            m 1ekbsb "If you do, just talk to me."

    return