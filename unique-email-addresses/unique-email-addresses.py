class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        bob = set()
        for x in emails:
            sub = ''
            if '+' in x:
                sub = x[0:x.index('+')]
            else:
                sub = x[0:x.index('@')]
            sub = sub.replace('.','')
            domain = x[x.index('@') + 1:]

            bob.add((sub,domain))
        return len(bob)