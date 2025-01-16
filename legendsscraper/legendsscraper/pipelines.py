import re

class LegendsScraperPipeline:
    def process_item(self, item, spider):
        # validations et traitement
        if not item.get('name') or not isinstance(item['name'], str):
            raise ValueError(f"Invalid or missing name: {item.get('name')}")

        if not item.get('role') or not isinstance(item['role'], str):
            item['role'] = 'Unknown'

        if not item.get('type') or not isinstance(item['type'], str):
            item['type'] = 'Unknown'

        try:
            item['move_speed'] = int(item['move_speed'])
            if item['move_speed'] < 0:
                raise ValueError
        except (ValueError, TypeError):
            item['move_speed'] = 0  

        try:
            item['attack_range'] = int(item['attack_range'])
            if item['attack_range'] < 0:
                raise ValueError
        except (ValueError, TypeError):
            item['attack_range'] = 0  

        if not item.get('image_url') or not re.match(r'^https?:\/\/', item['image_url']):
            item['image_url'] = 'https://via.placeholder.com/150'  

        return item

class LegendsHtmlPipeline:
    def open_spider(self, spider):
        # Un fichier HTML pour écrire les données
        self.file = open('legends.html', 'w', encoding='utf-8')
        # Écrire le header HTML
        self.file.write('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Liste des Champions</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #26565e, #0a8f77);
            margin: 0;
            padding: 20px;
            color: white;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        h1 {
            text-align: center;
            font-size: 2.5rem;
            margin-bottom: 20px;
        }
        .container {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
            gap: 20px;
            width: 100%;
            max-width: 1200px;
        }
        .card {
            background-color: white;
            color: black;
            border-radius: 8px;
            padding: 20px;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease;
        }
        .card:hover {
            transform: translateY(-5px);
        }
        .card img {
            width: 150px;
            height: 150px;
            border-radius: 50%;
            margin-bottom: 15px;
            object-fit: cover;
        }
        .pagination {
            margin: 20px 0;
            display: flex;
            gap: 10px;
        }
        .pagination button {
            background-color: #0a8f77;
            color: white;
            border: none;
            padding: 10px 15px;
            font-size: 16px;
            cursor: pointer;
            border-radius: 5px;
            transition: background-color 0.3s;
        }
        .pagination button:disabled {
            background-color: grey;
            cursor: not-allowed;
        }
        .pagination button:hover:not(:disabled) {
            background-color: #086f5f;
        }
    </style>
</head>
<body>
    <h1>Liste des Champions</h1>
    <div id="container" class="container"></div>
    <div class="pagination">
        <button id="prev" onclick="changePage(-1)">Précédent</button>
        <button id="next" onclick="changePage(1)">Suivant</button>
    </div>
    <script>
        const legends = [
        ''')

    def close_spider(self, spider):
        #les scripts de pagination et fermer le fichier HTML
        self.file.write('''
        ];
        const itemsPerPage = 12;
        let currentPage = 1;

        function renderPage() {
            const container = document.getElementById('container');
            container.innerHTML = '';
            const start = (currentPage - 1) * itemsPerPage;
            const end = start + itemsPerPage;
            const pageItems = legends.slice(start, end);

            pageItems.forEach(legend => {
                const card = document.createElement('div');
                card.className = 'card';
                card.innerHTML = `
                    <img src="${legend.image_url}" alt="${legend.name}">
                    <h2>${legend.name}</h2>
                    <p><strong>Rôle:</strong> ${legend.role}</p>
                    <p><strong>Type:</strong> ${legend.type}</p>
                    <p><strong>Move Speed:</strong> ${legend.move_speed}</p>
                    <p><strong>Attack Range:</strong> ${legend.attack_range}</p>
                `;
                container.appendChild(card);
            });

            document.getElementById('prev').disabled = currentPage === 1;
            document.getElementById('next').disabled = end >= legends.length;
        }

        function changePage(direction) {
            currentPage += direction;
            renderPage();
        }

        renderPage();
    </script>
</body>
</html>
''')
        self.file.close()

    def process_item(self, item, spider):
        # Ajouter chaque champion à la liste
        self.file.write(f'{item},\n')
        return item
