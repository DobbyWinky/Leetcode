class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        
        @lru_cache(None)
        def dp(i, remaining_width, curr_height):
            if i==n:
                return curr_height
            w=books[i][0]
            h=books[i][1]
            ans=dp(i+1, shelfWidth-w, h)+curr_height
            if w<=remaining_width:
                ans=min(ans, dp(i+1, remaining_width-w, max(curr_height, h)))
            return ans
        
        n=len(books)
        return dp(0,shelfWidth, 0)