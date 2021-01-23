
def part1(filepath):
    with open(filepath) as f:
        baglists = f.read().splitlines()
    gold_bag_list = []
    baglists = [word.replace('bags', 'bag') for word in baglists]
    # first level, bags that contain shiny gold bags
    def colorfinder(color, goldlist):
        for baglist in baglists:
            if color in baglist.split('contain')[1]:
                if baglist.split('contain')[0].strip() not in goldlist:
                    goldlist.append(baglist.split('contain')[0].strip())
    colorfinder('shiny gold', gold_bag_list)
    while True:
        n = len(gold_bag_list) # number of bags in list before trying to find more
        for color in gold_bag_list:
            colorfinder(color, gold_bag_list)
        if not len(gold_bag_list) > n: # break loop if n hasn't increased
            break 

    
    print(len(gold_bag_list))


def part2(filepath):
    with open(filepath) as f:
        baglists = f.read().splitlines()
    gold_bag_tree = {} # building a tree
    baglists = [word.replace('bags', 'bag') for word in baglists]
    # first level, bags that contain shiny gold bags
    def color_contains(color, tree):
        for baglist in baglists:
            if color in baglist.split('contain')[0]:
                if color not in gold_bag_tree.keys():
                    tree[color] = (baglist.split('contain ')[1].strip('.').split(', '))
    color_contains('shiny gold bag', gold_bag_tree)
    while True:
        n = len(gold_bag_tree) # number of bags in list before trying to find more
        for color in list(gold_bag_tree):
            for sub_color in gold_bag_tree[color]:
                color_contains(sub_color.split(' ', 1)[1], gold_bag_tree)
        if len(gold_bag_tree) == n: # break loop if n hasn't increased
            break 
    

    def bagcounter(color, tree):
        bagcount = 0
        for bag in tree[color]:
            if bag == 'no other bag':
                break
            bagcount += int(bag.split(' ', 1)[0])
            bagcount += int(bag.split(' ', 1)[0]) * bagcounter(bag.split(' ', 1)[1], tree)
        return bagcount
    
    all_bags = bagcounter('shiny gold bag', gold_bag_tree)
    
    print(all_bags)

if __name__ == '__main__':
    part1('/Users/ronaldauclair/Documents/personal/advent_of_code/day7/aocday7.txt')
    part2('/Users/ronaldauclair/Documents/personal/advent_of_code/day7/aocday7.txt')