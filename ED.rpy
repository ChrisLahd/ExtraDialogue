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

    m 1cke "This is a mod made by ChrisLad1 on GitHub"

    return
