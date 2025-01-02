# https://leetcode.com/problems/accounts-merge/?envType=company&envId=facebook&favoriteSlug=facebook-three-months&role=full-stack&status=TO_DO%2CATTEMPTED&difficulty=MEDIUM%2CEASY

from typing import List
from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        visited = set()
        adjacent = defaultdict(list)
        accountListSize = len(accounts)

        def dfs(mergedAccount: List[str], email: str):
            visited.add(email)
            mergedAccount.append(email)

            if email not in adjacent:
                return
            
            for neighbor in adjacent[email]:
                if neighbor not in visited:
                    dfs(mergedAccount, neighbor)

        for account in accounts:
            accountSize = len(account)

            accountFirstEmail = account[1]

            for j in range(2, accountSize):
                accountEmail = account[j]

                if accountFirstEmail not in adjacent:
                    adjacent[accountFirstEmail] = []

                adjacent[accountFirstEmail].append(accountEmail)

                if accountEmail not in adjacent:
                    adjacent[accountEmail] = []

                adjacent[accountEmail].append(accountFirstEmail)

        mergedAccounts = []

        for account in accounts:
            accountName = account[0]
            accountFirstEmail = account[1]

            if accountFirstEmail not in visited:
                mergedAccount = []
                mergedAccount.append(accountName)
                dfs(mergedAccount, accountFirstEmail)

                tmp = mergedAccount[1:]
                tmp.sort()
                tmp.insert(0, mergedAccount[0])
                mergedAccounts.append(tmp)

        return mergedAccounts

class DSU:
    representative = []
    size = []

    def __init__(self, size):
        self.representative = [0] * size
        self.size = [0] * size

        for i in range(0, size):
            self.representative[i] = i
            self.size[i] = i

    def findRepresentative(self, x: int) -> int:
        if x == self.representative[x]:
            return x
        
        self.representative[x] = self.findRepresentative(self.representative[x])
        return self.representative[x]
    
    def unionBySize(self, a: int, b: int):
        representativeA = self.findRepresentative(a)
        representativeB = self.findRepresentative(b)

        if representativeA == representativeB:
            return
        
        if self.size[representativeA] >= self.size[representativeB]:
            self.size[representativeA] += self.size[representativeB]
            self.representative[representativeB] = representativeA
        else:
            self.size[representativeB] += self.size[representativeA]
            self.representative[representativeA] = representativeB

class Solution2:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        accountListSize = len(accounts)
        dsu = DSU(accountListSize)

        emailGroup = {}

        for i in range(0, accountListSize):
            accountSize = len(accounts[i])

            for j in range(1, accountSize):
                email = accounts[i][j]
                accountName = accounts[i][0]

                if email not in emailGroup:
                    emailGroup[email] = i
                else:
                    dsu.unionBySize(i, emailGroup[email])

        components = {}

        for email in emailGroup:
            group = emailGroup[email]
            groupRep = dsu.findRepresentative(group)

            if groupRep not in components:
                components[groupRep] = []
            
            components[groupRep].append(email)

        mergedAccounts = []

        for group in components:
            component = components[group]
            component.sort()
            component.insert(0, accounts[group][0])
            mergedAccounts.append(component)

        return mergedAccounts

s = Solution2()

accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]

print(s.accountsMerge(accounts))

accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]

print(s.accountsMerge(accounts))
