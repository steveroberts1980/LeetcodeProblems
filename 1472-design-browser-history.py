class BrowserHistory:

    def __init__(self, homepage: str):
        self.forward_history = []
        self.backward_history = []
        self.current_site = homepage

    def visit(self, url: str) -> None:
        self.forward_history = []
        self.backward_history.append(self.current_site)
        self.current_site = url

    def back(self, steps: int) -> str:
        for i in range(steps):
            if not len(self.backward_history):
                return self.current_site

            self.forward_history.append(self.current_site)
            self.current_site = self.backward_history.pop()

        return self.current_site

    def forward(self, steps: int) -> str:
        for i in range(steps):
            if not len(self.forward_history):
                return self.current_site

            self.backward_history.append(self.current_site)
            self.current_site = self.forward_history.pop()

        return self.current_site


browserHistory = BrowserHistory("leetcode.com");
browserHistory.visit("google.com");       # You are in "leetcode.com". Visit "google.com"
browserHistory.visit("facebook.com");     # You are in "google.com". Visit "facebook.com"
browserHistory.visit("youtube.com");      # You are in "facebook.com". Visit "youtube.com"
print(browserHistory.back(1));                   # You are in "youtube.com", move back to "facebook.com" return "facebook.com"
print(browserHistory.back(1));                   # You are in "facebook.com", move back to "google.com" return "google.com"
print(browserHistory.forward(1));                # You are in "google.com", move forward to "facebook.com" return "facebook.com"
browserHistory.visit("linkedin.com");     # You are in "facebook.com". Visit "linkedin.com"
print(browserHistory.forward(2));                # You are in "linkedin.com", you cannot move forward any steps.
print(browserHistory.back(2));                   # You are in "linkedin.com", move back two steps to "facebook.com" then to "google.com". return "google.com"
print(browserHistory.back(7));                   # You are in "google.com", you can move back only one step to "leetcode.com". return "leetcode.com"
