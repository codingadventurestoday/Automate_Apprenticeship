#this small app ulitizes Python's module, urllib, to read through website's robot.txt page

from urllib import robotparser 

robot_parser = robotparser.RobotFileParser()

def prepare(robot_txt_url):
    robot_parser.set_url(robot_txt_url)
    robot_parser.read()

def is_allowed(target_url, user_agent = '*'):
    return robot_parser.can_fetch(user_agent, target_url)

if __name__ == '__main__':
    prepare('<<<url here>>>')

    print(is_allowed('<<<url here plus whatever page you are checking'))
