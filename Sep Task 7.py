import os

class BlogPostCMS:
    def __init__(self):
        self.blog_post_directory = "blog_posts"
        if not os.path.exists(self.blog_post_directory):
            os.mkdir(self.blog_post_directory)

    def create_blog_post(self):
        title = input("Enter the title of the blog post: ")
        content = input("Enter the content of the blog post: ")

        file_path = os.path.join(self.blog_post_directory, f"{title}.txt")

        if os.path.exists(file_path):
            print(f"Blog post '{title}' already exists.")
        else:
            with open(file_path, "w") as file:
                file.write(content)
            print(f"Blog post '{title}' created successfully!")

    def read_blog_post(self):
        title = input("Enter the title of the blog post you want to read: ")
        file_path = os.path.join(self.blog_post_directory, f"{title}.txt")

        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                content = file.read()
                print(content)
        else:
            print(f"Blog post '{title}' does not exist.")

    def edit_blog_post(self):
        title = input("Enter the title of the blog post you want to edit: ")
        file_path = os.path.join(self.blog_post_directory, f"{title}.txt")

        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                existing_content = file.read()

            new_content = input("Enter the new content for the blog post: ")

            with open(file_path, "w") as file:
                file.write(new_content)

            print(f"Blog post '{title}' edited successfully!")
        else:
            print(f"Blog post '{title}' does not exist.")

    def main_menu(self):
        while True:
            print("\nMain Menu:")
            print("1. Create a Blog Post")
            print("2. Read a Blog Post")
            print("3. Edit a Blog Post")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.create_blog_post()
            elif choice == "2":
                self.read_blog_post()
            elif choice == "3":
                self.edit_blog_post()
            elif choice == "4":
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    cms = BlogPostCMS()
    cms.main_menu()
