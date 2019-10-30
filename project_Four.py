#Create on 10/22/19 by: Adrian Lopez 
#Project 4; Data Structures 2302, Instructor: Diego Aguirre, T.A: Gerardo Barraza
#Purpose: Implement a B-Tree

import string
from BTrees import BTreeNode
from BTrees import BTree

#///////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////
    
def main():

    #2  
    def similarity_of_words(word_one, word_two, tree):
        word_one_n = tree.search(word_one)
        word_two_n = tree.search(word_two)
        
        word_one_embed = word_one_n.get_embedding()
        word_two_embed = word_two_n.get_embedding()

        if word_one_embed is not None and word_two_embed is not None:
            top = 0
            bottom_one = 0
            bottom_two = 0
            embed_len = len(word_one_embed)
            for i in range(embed_len):
                top += (word_one_embed[i] * word_two_embed[i])
                bottom_one += word_one_embed[i].abs()
                bottom_two += word_two_embed[i].abs()
            return (top / (bottom_one * bottom_two))
        return -1
    
    def similarity_from_file(file_name, tree):
        with open(file_name) as file:
            for line in file:
                given_tree = tree
                
                words = line.split(" ")
                word_one = words[0]
                word_two = words[1]
                similarity = 0
                similarity = similarity_of_words(word_one, word_two, given_tree)
                print("Similarity of " + str(word_one) + " and " + str(word_two) + " = " + str(similarity))

    #3 a)
    def number_of_nodes(node):
        if node is None:
            return 0
        count = 0
        for i in range(len(node.keys)):
            count += 1
        return count

    #3 b)
    def get_height(node):
        return b_tree.height(node_words)

    #3 c)
    def words_stored_in_tree(node, given_file):
        if node is None:
            return 0
        words_stored_in_tree(node.left, given_file)
        given_file.write(node.key + "\n")
        words_stored_in_tree(node.right, given_file)
    
    #3 d)
    # Given a desired depth, generate a file with all the keys that have that depth, in ascending order.
    def depth_of_keys(node, depth, file_depth):
        if depth < 0:
            return
        if depth == 0:
            for i in range(len(node.keys)):
                file_depth.write(node.keys + "\n")
        if node is None:
            return -1
        
        depth_of_keys(node.left, depth-1, file_depth)
        depth_of_keys(node.right, depth-1, file_depth)
    
    #////////////////////////////////////////////////////////
    
    print("Enter 0 to continue")

    file_name = "/Users/adrianlopez/Desktop/CS 2302/glove.6b.50d.txt"
    user_input = input()
    b_tree = BTree()

    if user_input == '0':
        try:
            with open(file_name, encoding = "utf8") as file:
                alphabet = list(string.ascii_letters)
                for line in file:
                    array = line.split(" ")
                    word = array[0]
                    if alphabet.__contains__(word[0]):
                        nums = []
                                    #slice
                        for num in array[1:]:
                            nums.append(float(num))
                        node_words = BTreeNode(word, nums)
                        for i in range(len(node_words) - 1):
                            b_tree.insert(i, node_words)
                            #b_tree.print()
                            # print("Number of nodes in tree = ", number_of_nodes(b_tree.root))
                            # print("Height of tree = ", b_tree.height(b_tree.root))
                            # print("Words in tree; ascending order: ")
                            # words_stored_in_tree(b_tree, file_name)
                            # print("Keys at desired path: ")
                            # depth_of_keys(b_tree, 0, 0)
        except FileNotFoundError:
            print("File not Found")
            exit()
        return b_tree
    else:
        print("Incorrect value, goodbye.")
        return
    return

if __name__ == "__main__":
    main()



