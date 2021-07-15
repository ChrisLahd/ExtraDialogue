# Register the submod
init -990 python:
    store.mas_submod_utils.Submod(
        author="ChrisLad",
        name="Extra Dialogue",
        description="Adds fitting dialogue to Monika",
        version="1.0.2"
    )

# Register the updater
init -989 python:
    if store.mas_submod_utils.isSubmodInstalled("Submod Updater Plugin"):
        store.sup_utils.SubmodUpdater(
            submod="Extra Dialogue",
            user_name="ChrisLad1",
            repository_name="ExtraDialogue",
            update_dir="game",
            attachment_id=None
        )
    
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_truthful",
            category=["ED"],
            prompt="Being together forever",
            pool=True,
            random=True,
            unlocked=True
        )
    )

label monika_truthful:

    $ amt = mas_getEV("monika_truthful")
        
    if amt.shown_count >= 3 or EV_ACT_RANDOM != True:

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
            category=["ED"],
            prompt="Credits",
            pool=True,
            random=True,
            unlocked=True
        )
    )

label monika_promotional:

    m 1enc "This is a mod made by ChrisLad1 on GitHub"
    m 7enc "You can view it {a="https://GitHub.com/ChrisLad1/ExtraDialogue"} Here"
    m 7rkc "That is if you haven't somehow downloaded this already."

    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_proud",
            category=["ED"],
            prompt=["I did something today."]
            pool=True,
            unlocked=True
        )
    )

label monika_proud:

    m 1ekc "Wow!, what did you do [player]?{nw}"
    $ _history_list.pop()

    menu:

        m "Wow!, what did you do [player]?{fast}"

        "I achieved one of my goals.":

            m 1enc "Wow!, I am so happy for you!"
            m 7enc "You really do amaze me [player]!"
            m 7rkc "Just remember, never stop trying even if you are ahead of yourself. That is the best way to keep a self-motive mindset."
            m 1enc "Which means you can share more of your acomplishments with me~"
            m 1enc "Ehehe~"

        "I went somewhere.":

            m 1enc "[player], thats great!"
            m 1ekc "[player], you didn't tell me we were going out though."
            m 1rkc "I-It's fine but... I wish I knew is all."
            m 7enc "All the matter is that you are here now, [player]~"

        "More coming soon!":

            m 1enc "You heard him~ :)"
            
