class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        emailset = set()
        for email in emails:
            local,domain = email.split('@')
            local = local.split('+')[0].replace('.','')
            concatenate = local + '@' + domain

            emailset.add(concatenate)
        return len(emailset)
           