import datetime

class Channel():
    
    def __init__(self, name):
    
        self.name = name
        self.subscribers = []
        self.videos = []
    
    def subscribe(self, user):
        
        self.subscribers.append(user)
        user.channels.append(self)
        
    def unsubscribe(self, user):
    
        self.subscribers.remove(user)
        user.channels.remove(self)
    
    def notifySubscribers(self):

        for subscriber in self.subscribers:
            subscriber.update()
            
    def publish(self, titre_de_video):
        
        self.videos.append({
            "titre": titre_de_video,
            "date": datetime.datetime.now()
        })
        self.notifySubscribers()


class User():
    
    def __init__(self, name):
        
        self.name = name
        self.channels = []
        
    def update(self):
        
        # Obtenir la liste de toutes les vidéos de tous les channels auquel on a subscribe  ...
        all_videos = []
        for channel in self.channels:
            
            # Pour chaque video, on veut garder le nom du channel d'origine. On le rajoute donc à la volée :
            videos_for_this_channel = channel.videos.copy()
            for video in videos_for_this_channel:
                video["channel"] = channel.name
            
            all_videos += videos_for_this_channel
        
        # ... ordonné par date de publication
        all_videos_sorted = sorted(all_videos, key=lambda v: v["date"], reverse=True)
        
        # ... et seulement les 3 les plus récentes
        most_recent_videos = all_videos_sorted[:3]
        
        with open(f"most_recent_videos_for_{self.name}.txt", "w") as f:
            for video in most_recent_videos:
                f.write(f"[{video['channel']}] {video['titre']} (publiée le {video['date']}) \n")
        

arte = Channel("ARTE")
cestpassorcier = Channel("c'est pas sorcier")
videodechat = Channel("video de chat")

alice = User("alice")
bob = User("bob")
charlie = User("charlie")

arte.subscribe(alice)
cestpassorcier.subscribe(alice)
cestpassorcier.subscribe(bob)
videodechat.subscribe(bob)
videodechat.subscribe(charlie)

cestpassorcier.publish("Le système solaire")
arte.publish("La grenouille, un animal extraordinaire")
cestpassorcier.publish("Le génie des fourmis")
videodechat.publish("Video de chat qui fait miaou")
cestpassorcier.publish("Les chateaux forts")