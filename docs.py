import os
import yaml

def generate_navigation(root_dir):
    navigation = []
    for root, dirs, files in os.walk(root_dir):
        for dir_name in dirs:
            path = os.path.relpath(os.path.join(root, dir_name), root_dir)
            navigation.append({
                'title': dir_name,
                'url': f'/{path}/'
            })
    return navigation

if __name__ == "__main__":
    root_directory = '.'  # Diretório raiz do seu repositório
    navigation_data = generate_navigation(root_directory)
    with open('docs.yml', 'w') as file:
        yaml.dump(navigation_data, file, default_flow_style=False)
