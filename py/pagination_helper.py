# TODO: complete this class

class PaginationHelper:

    # The constructor takes in an array of items and an integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page

    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)

    # returns the number of pages
    def page_count(self):
        result = 0
        tmp = self.collection
        while tmp:
            tmp = tmp[self.items_per_page::1]
            result += 1
        del tmp
        return result

    def list_of_page(self):
        tmp = self.collection
        result = []
        while tmp:
            result.append(tmp[0:self.items_per_page])
            tmp = tmp[self.items_per_page::1]
        del tmp
        return result

    # returns the number of items on the given page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        if page_index >= self.page_count() or page_index < 0:
            return -1
        else:
            return len(self.list_of_page()[page_index])

    # determines what page an item at the given index is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        if item_index > len(self.collection) - 1 or item_index < 0:
            return -1

        search_item = self.collection[item_index]
        tmp = self.list_of_page()
        for page in tmp:
            if search_item in page:
                return tmp.index(page)


a = PaginationHelper([i for i in range(24)], 6)
print(a.page_index(7))



# Instructions

# For this exercise you will be strengthening your page-fu mastery.
# You will complete the PaginationHelper class, which is a utility class helpful for querying paging information related to an array.

# The class is designed to take in an array of values and an integer indicating how many items will be allowed per each page.
# The types of values contained within the collection/array are not relevant.

# The following are some examples of how this class is used:

# helper = PaginationHelper(['a','b','c','d','e','f'], 4)
# helper.page_count() # should == 2
# helper.item_count() # should == 6
# helper.page_item_count(0) # should == 4
# helper.page_item_count(1) # last page - should == 2
# helper.page_item_count(2) # should == -1 since the page is invalid

# # page_index takes an item index and returns the page that it belongs on
# helper.page_index(5) # should == 1 (zero based index)
# helper.page_index(2) # should == 0
# helper.page_index(20) # should == -1
# helper.page_index(-10) # should == -1 because negative indexes are invalid
