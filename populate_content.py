import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'peertopeer.settings')
django.setup()

from core.models import InternationalPage, VolunteeringPage, ProjectsPage

def populate():
    # International Page
    intl_page, created = InternationalPage.objects.get_or_create(id=1)
    intl_page.title_uk = "Міжнародна діяльність"
    intl_page.title_en = "International Activity"
    intl_page.content_uk = """
    <h2>Співпраця з міжнародними партнерами</h2>
    <p>Наш фонд активно співпрацює з міжнародними організаціями для реалізації масштабних гуманітарних та освітніх проєктів. Ми віримо, що об'єднання зусиль на глобальному рівні дозволяє досягати значних змін.</p>
    
    <h3>Наші ключові напрямки:</h3>
    <ul>
        <li><strong>Гуманітарна допомога:</strong> Залучення ресурсів від європейських донорів для підтримки постраждалих регіонів.</li>
        <li><strong>Обмін досвідом:</strong> Участь у міжнародних конференціях та стажування для наших волонтерів.</li>
        <li><strong>Грантові програми:</strong> Реалізація проєктів за підтримки фондів ЄС та США.</li>
    </ul>

    <h3>Партнери</h3>
    <p>Ми пишаємося співпрацею з такими організаціями як USAID, UNICEF та Червоний Хрест. Разом ми будуємо краще майбутнє.</p>
    """
    intl_page.content_en = """
    <h2>Cooperation with International Partners</h2>
    <p>Our foundation actively cooperates with international organizations to implement large-scale humanitarian and educational projects. We believe that uniting efforts on a global level allows for significant changes.</p>
    
    <h3>Our Key Directions:</h3>
    <ul>
        <li><strong>Humanitarian Aid:</strong> Attracting resources from European donors to support affected regions.</li>
        <li><strong>Experience Exchange:</strong> Participation in international conferences and internships for our volunteers.</li>
        <li><strong>Grant Programs:</strong> Implementation of projects supported by EU and USA funds.</li>
    </ul>

    <h3>Partners</h3>
    <p>We are proud to cooperate with organizations such as USAID, UNICEF, and the Red Cross. Together we are building a better future.</p>
    """
    intl_page.save()
    print("International Page updated.")

    # Volunteering Page
    vol_page, created = VolunteeringPage.objects.get_or_create(id=1)
    vol_page.title_uk = "Волонтерство"
    vol_page.title_en = "Volunteering"
    vol_page.content_uk = """
    <h2>Приєднуйся до команди змін!</h2>
    <p>Волонтери — це серце нашого фонду. Щодня сотні небайдужих людей віддають свій час та енергію, щоб допомагати тим, хто цього потребує.</p>

    <h3>Як ви можете допомогти?</h3>
    <ul>
        <li><strong>Логістика:</strong> Допомога у сортуванні та доставці гуманітарних вантажів.</li>
        <li><strong>Професійні навички:</strong> Юридичні консультації, психологічна підтримка, IT-послуги.</li>
        <li><strong>Організація подій:</strong> Допомога у проведенні благодійних заходів та акцій.</li>
    </ul>

    <h3>Чому варто стати волонтером?</h3>
    <p>Ви отримаєте унікальний досвід, нових друзів та відчуття причетності до великої справи. Ми проводимо регулярні тренінги та зустрічі для нашої спільноти.</p>
    
    <p><strong>Заповнюйте анкету та ставайте частиною нашої родини!</strong></p>
    """
    vol_page.content_en = """
    <h2>Join the Change Team!</h2>
    <p>Volunteers are the heart of our foundation. Every day, hundreds of caring people dedicate their time and energy to helping those in need.</p>

    <h3>How can you help?</h3>
    <ul>
        <li><strong>Logistics:</strong> Assistance in sorting and delivering humanitarian cargo.</li>
        <li><strong>Professional Skills:</strong> Legal consultations, psychological support, IT services.</li>
        <li><strong>Event Organization:</strong> Assistance in holding charity events and campaigns.</li>
    </ul>

    <h3>Why become a volunteer?</h3>
    <p>You will gain unique experience, new friends, and a sense of belonging to a great cause. We hold regular trainings and meetings for our community.</p>
    
    <p><strong>Fill out the form and become part of our family!</strong></p>
    """
    vol_page.save()
    print("Volunteering Page updated.")

    # Projects Page
    proj_page, created = ProjectsPage.objects.get_or_create(id=1)
    proj_page.title_uk = "Наші Проєкти"
    proj_page.title_en = "Our Projects"
    proj_page.content_uk = """
    <h2>Реалізовані та поточні ініціативи</h2>
    <p>Ми реалізуємо проєкти, спрямовані на підтримку освіти, медицини та соціального захисту. Кожен проєкт — це крок до вирішення конкретної проблеми.</p>

    <h3>Поточні проєкти</h3>
    <div class="project-item">
        <h4>Школа Лідерів</h4>
        <p>Освітня програма для молоді, спрямована на розвиток лідерських якостей та навичок проєктного менеджменту.</p>
    </div>
    <div class="project-item">
        <h4>Медичний десант</h4>
        <p>Забезпечення лікарень у віддалених регіонах необхідним обладнанням та медикаментами.</p>
    </div>

    <h3>Завершені проєкти</h3>
    <div class="project-item">
        <h4>Тепло для кожного</h4>
        <p>Забезпечення генераторами та обігрівачами 50 притулків для переселенців.</p>
    </div>
    """
    proj_page.content_en = """
    <h2>Implemented and Current Initiatives</h2>
    <p>We implement projects aimed at supporting education, medicine, and social protection. Each project is a step towards solving a specific problem.</p>

    <h3>Current Projects</h3>
    <div class="project-item">
        <h4>School of Leaders</h4>
        <p>Educational program for youth aimed at developing leadership qualities and project management skills.</p>
    </div>
    <div class="project-item">
        <h4>Medical Landing</h4>
        <p>Providing hospitals in remote regions with necessary equipment and medicines.</p>
    </div>

    <h3>Completed Projects</h3>
    <div class="project-item">
        <h4>Warmth for Everyone</h4>
        <p>Providing generators and heaters to 50 shelters for displaced persons.</p>
    </div>
    """
    proj_page.save()
    print("Projects Page updated.")

if __name__ == '__main__':
    populate()
