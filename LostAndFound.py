class LostAndFound:
    def __init__(self):
        self.lost_items = []
        self.found_items = []

    def add_lost_item(self, item_name, description, location, contact_info):
        self.lost_items.append({
            "item_name": item_name,
            "description": description,
            "location": location,
            "contact_info": contact_info
        })

    def add_found_item(self, item_name, description, location, contact_info):
        self.found_items.append({
            "item_name": item_name,
            "description": description,
            "location": location,
            "contact_info": contact_info
        })

    def display_lost_items(self):
        if not self.lost_items:
            print("没有失物信息。")
        else:
            print("失物信息：")
            for item in self.lost_items:
                print(f"物品名称：{item['item_name']}")
                print(f"描述：{item['description']}")
                print(f"丢失地点：{item['location']}")
                print(f"联系方式：{item['contact_info']}")
                print("-" * 20)

    def display_found_items(self):
        if not self.found_items:
            print("没有招领信息。")
        else:
            print("招领信息：")
            for item in self.found_items:
                print(f"物品名称：{item['item_name']}")
                print(f"描述：{item['description']}")
                print(f"发现地点：{item['location']}")
                print(f"联系方式：{item['contact_info']}")
                print("-" * 20)


def main():
    platform = LostAndFound()
    while True:
        print("\n欢迎来到校园失物招领平台")
        print("1. 发布失物信息")
        print("2. 发布招领信息")
        print("3. 查看失物信息")
        print("4. 查看招领信息")
        print("5. 退出")
        choice = input("请输入您的选择：")

        if choice == "1":
            item_name = input("请输入丢失物品名称：")
            description = input("请输入物品描述：")
            location = input("请输入丢失地点：")
            contact_info = input("请输入联系方式：")
            platform.add_lost_item(item_name, description, location, contact_info)
            print("失物信息已发布。")

        elif choice == "2":
            item_name = input("请输入发现物品名称：")
            description = input("请输入物品描述：")
            location = input("请输入发现地点：")
            contact_info = input("请输入联系方式：")
            platform.add_found_item(item_name, description, location, contact_info)
            print("招领信息已发布。")

        elif choice == "3":
            platform.display_lost_items()

        elif choice == "4":
            platform.display_found_items()

        elif choice == "5":
            print("感谢使用校园失物招领平台，再见！")
            break

        else:
            print("无效的选择，请重新输入。")


if __name__ == "__main__":
    main()