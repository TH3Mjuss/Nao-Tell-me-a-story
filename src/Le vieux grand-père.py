# -*- coding: utf-8 -*-
from naoqi import ALProxy
import argparse

"""
\pau=xxx\    --> pause time (in ms)
\vct=xxx\    --> manage voice pitch 50 to 200% (default 100%)
\rspd=xxx\   --> voice speed 50 to 400% (default 100%)
\vol=xxx\    --> manage volume 1to 100%
"""
def main (IP, PORT=9559):
    # Declare the proxies we will be using
    atts = ALProxy("ALAnimatedSpeech", IP, PORT)
    motion = ALProxy("ALMotion", IP, PORT)
    proxyPosture = ALProxy("ALRobotPosture", IP, PORT)
    # Wake up the robot to make it able to move (enable the motors)
    motion.wakeUp()
    # Configure the body language
    configuration = {"bodyLanguageMode":"contextual"}
    # Text to be read
    atts.say("Bonjour, je vais te raconter l'histoire du vieux grand-père.\\pau=1500\\")
    atts.say("\\rspd=90\\Il était une fois un pauvre homme bien vieux, \\pau=200\\qui avait les yeux trouble, \\pau=200\\"\
            "l’oreille dure et les genoux tremblants. \\pau=600\\Quand il était à table,\\pau=200\\ il pouvait à peine tenir "\
            "sa cui yère ;\\pau=450\\ il reaipandait de la soupe sur la nappe,\\pau=200\\ et quelquefois mème en laissait échapper "\
            "de sa bouche.\\pau=600\\ La femme de son fils,\\pau=200\\ et son fils lui-mème en avaient pris un grand \\rspd=85\\daigoût, \\pau=200\\"\
            "\\rspd=100\\et à la fin ils le reléguaire dans un coin derrière le poil, \\pau=200\\ où ils lui donnaient à manger une "\
            "chaitive pitance dans une vieille écuelle de terre.\\pau=600\\ Le vieillard avaient souvent les larmes aux yeux,\\pau=200\\ "\
            "et regardait tristement du coter de la table...\\pau=800\\", configuration)
    atts.say("\\rspd=90\\Un jour, \\pau=200\\ l'écuelle,\\pau=200\\ que tenaient mal ses mains tremblantes,\\pau=200\\ tomba À terre et se brisa."\
            "\\pau=600\\La jeune femme s'emporta en reproches:\\pau=400\\ il n'osa rien répondre et baissa la tête en soupirant.\\pau=600\\"\
            "On lui \\rspd=90\\acheuta \\rspd=100\\ pour deux liards une écuelle de bois dans laquelle désormais on lui donnait à manger."\
            "\\pau=800\\", configuration)
    atts.say("\\rspd=90\\Quelques jours après,\\pau=200\\ son fils et sa belle-fille virent leur enfant qui avait quatre ans,\\pau=200\\ occupé \\pau=120\\"\
            "à assembler par terre de petites planchettes.\\pau=600\\ \\rspd=95\\ \\vct=70\\Que fais-tu là ?\\vct=100\\ \\rspd=100\\ Demanda "\
            "son père.\\pau=600\\ \\vct=150\\C'est un auget, \\pau=200\\ \\vct=100\\ répondit l'enfant,\\pau=200\\ \\vct=150\\pour donner À manger "\
            "à papa et \\rspd=85\\maman quand ils seront vieux.\\vct=100\\ \\pau=800\\", configuration)
    atts.say("\\rspd=90\\Le mari et la femme se regardère un instant sans rien dire,\\pau=200\\ puis ils se mirent à pleurer, \\pau=200\\ reprirent le "\
            "vieux grand-père à table,\\pau=200\\ et désormais le firent toujours manger à table avec eux,\\pau=200\\ sans plus jamais le rudoyer.", configuration)
    # Get the current posture of the robot
    posture = proxyPosture.getPostureFamily()
    # Set the robot to a 'Standard posture'
    if posture == "Standing":
            proxyPosture.goToPosture("Stand", 0.5)
    else:
            proxyPosture.goToPosture("Sit", 0.5)
    # Make it rest (disable the motors)
    motion.rest()

    print("done \n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str,
                        help="Robot ip address")
    parser.add_argument("--port", type=int,
                        help="Robot port number (Default: 9559)")

    args = parser.parse_args()
    main(args.ip, args.port)
