from getpass import getpass
import instaloader

username = input("Username: ")
password = getpass("Password: ")
follower_usernem = input("Follower_usernem: ")

L = instaloader.Instaloader()
L.login(username, password)
profile = instaloader.Profile.from_username(L.context, follower_usernem)

file = open("followers.txt", "r")
old_followers = []
for line in file:
    old_followers.append(line.strip())
file.close()

new_followers = []
for follower in profile.get_followers():
    new_followers.append(follower.username)

for new_follower in new_followers:
    if new_follower not in old_followers:
        print(new_follower)

f = open("followers.txt", "w")
for new_follower in new_followers:
    file.write(new_follower + "\n")
file.close()