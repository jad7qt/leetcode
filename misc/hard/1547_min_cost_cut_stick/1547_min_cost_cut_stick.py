class Solution(object):
  def minCost(self, n, cuts):
    """
    :type n: int
    :type cuts: List[int]
    :rtype: int
    """

    # Order the list of cuts
    cuts.sort()
    mem = {}
    def minCostRecurse(self, n, cuts):
      if len(cuts) < 1:
        return 0
      elif (len(cuts) == 1):
        return n
      elif (n, tuple(cuts)) in mem:
        return mem[(n, tuple(cuts))]
      
      initial_min = float('inf')
      # Cut and recurse for both ends, rebase each 
      for i in range(len(cuts)):
        # For each cut, calculate min cost
        # First stick is 0 - cut, second is cut - n
        second_list = [item - cuts[i] for item in cuts[i+1:]]
        cost = n + minCostRecurse(self, cuts[i], cuts[:i]) + minCostRecurse(self, n-cuts[i], second_list)
        initial_min = min(cost, initial_min)
      mem[(n, tuple(cuts))] = initial_min
      return initial_min
  
    return minCostRecurse(self, n, cuts)