import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'peertopeer.settings')
django.setup()

from core.models import InternationalPage, VolunteeringPage, ProjectsPage, StatutPage

def populate():
    # --- Statut Page ---
    statut_page, created = StatutPage.objects.get_or_create(id=1)
    statut_page.title_uk = "Статутна діяльність"
    statut_page.title_en = "Statutory Activity"
    
    statut_html_uk = """
    <section class="relative py-20 overflow-hidden bg-white">
        <div class="relative z-10 max-w-4xl mx-auto text-center px-4">
            <div class="inline-block px-4 py-1 rounded-full bg-blue-100 text-[#0057B8] font-bold text-sm mb-4 uppercase tracking-wider">Прозорість</div>
            <h1 class="text-4xl md:text-6xl font-heading font-bold text-[#212529] mb-6">Офіційні документи</h1>
            <p class="text-xl text-gray-600 max-w-2xl mx-auto">Ми працюємо відкрито та прозоро. Тут ви можете ознайомитись з нашими установчими документами та звітами.</p>
        </div>
    </section>
    <section class="py-12 max-w-6xl mx-auto px-4">
        <div class="grid md:grid-cols-3 gap-8">
            <div class="bg-gray-50 p-8 rounded-2xl border border-gray-100 hover:shadow-md transition">
                <h3 class="text-xl font-bold text-[#212529] mb-2">Статут Фонду</h3>
                <p class="text-gray-600 mb-4">Основний документ, що регулює діяльність організації.</p>
                <a href="#" class="text-[#0057B8] font-bold hover:underline">Завантажити PDF &rarr;</a>
            </div>
            <div class="bg-gray-50 p-8 rounded-2xl border border-gray-100 hover:shadow-md transition">
                <h3 class="text-xl font-bold text-[#212529] mb-2">Виписка з ЄДР</h3>
                <p class="text-gray-600 mb-4">Підтвердження державної реєстрації благодійної організації.</p>
                <a href="#" class="text-[#0057B8] font-bold hover:underline">Завантажити PDF &rarr;</a>
            </div>
            <div class="bg-gray-50 p-8 rounded-2xl border border-gray-100 hover:shadow-md transition">
                <h3 class="text-xl font-bold text-[#212529] mb-2">Річний звіт 2024</h3>
                <p class="text-gray-600 mb-4">Детальний звіт про надходження та використання коштів.</p>
                <a href="#" class="text-[#0057B8] font-bold hover:underline">Завантажити PDF &rarr;</a>
            </div>
        </div>
    </section>
    """
    
    statut_html_en = """
    <section class="relative py-20 overflow-hidden bg-white">
        <div class="relative z-10 max-w-4xl mx-auto text-center px-4">
            <div class="inline-block px-4 py-1 rounded-full bg-blue-100 text-[#0057B8] font-bold text-sm mb-4 uppercase tracking-wider">Transparency</div>
            <h1 class="text-4xl md:text-6xl font-heading font-bold text-[#212529] mb-6">Official Documents</h1>
            <p class="text-xl text-gray-600 max-w-2xl mx-auto">We work openly and transparently. Here you can find our founding documents and reports.</p>
        </div>
    </section>
    <section class="py-12 max-w-6xl mx-auto px-4">
        <div class="grid md:grid-cols-3 gap-8">
            <div class="bg-gray-50 p-8 rounded-2xl border border-gray-100 hover:shadow-md transition">
                <h3 class="text-xl font-bold text-[#212529] mb-2">Foundation Statute</h3>
                <p class="text-gray-600 mb-4">The main document regulating the organization's activities.</p>
                <a href="#" class="text-[#0057B8] font-bold hover:underline">Download PDF &rarr;</a>
            </div>
            <div class="bg-gray-50 p-8 rounded-2xl border border-gray-100 hover:shadow-md transition">
                <h3 class="text-xl font-bold text-[#212529] mb-2">Registration Extract</h3>
                <p class="text-gray-600 mb-4">Confirmation of state registration of the charitable organization.</p>
                <a href="#" class="text-[#0057B8] font-bold hover:underline">Download PDF &rarr;</a>
            </div>
            <div class="bg-gray-50 p-8 rounded-2xl border border-gray-100 hover:shadow-md transition">
                <h3 class="text-xl font-bold text-[#212529] mb-2">Annual Report 2024</h3>
                <p class="text-gray-600 mb-4">Detailed report on funds received and used.</p>
                <a href="#" class="text-[#0057B8] font-bold hover:underline">Download PDF &rarr;</a>
            </div>
        </div>
    </section>
    """
    statut_page.content_uk = statut_html_uk
    statut_page.content_en = statut_html_en
    statut_page.save()
    print("Statut Page updated.")

    # --- International Page ---
    intl_page, created = InternationalPage.objects.get_or_create(id=1)
    intl_page.title_uk = "Міжнародна діяльність"
    intl_page.title_en = "International Activity"
    
    intl_html_uk = """
    <section class="relative py-20 overflow-hidden">
        <div class="relative z-10 max-w-4xl mx-auto text-center px-4">
            <div class="inline-block px-4 py-1 rounded-full bg-yellow-100 text-yellow-800 font-bold text-sm mb-4 uppercase tracking-wider">Співпраця</div>
            <h1 class="text-4xl md:text-6xl font-heading font-bold text-[#212529] mb-6">Міжнародні Партнери</h1>
            <p class="text-xl text-gray-600 max-w-2xl mx-auto">Ми об'єднуємо зусилля з глобальними організаціями для реалізації масштабних гуманітарних проєктів.</p>
        </div>
    </section>
    <section class="py-12 max-w-6xl mx-auto px-4 bg-gray-50 rounded-3xl">
        <div class="grid md:grid-cols-3 gap-8 text-center">
            <div class="p-6">
                <h3 class="text-2xl font-bold text-[#0057B8] mb-2">USAID</h3>
                <p class="text-gray-600">Підтримка демократії та економічного розвитку.</p>
            </div>
            <div class="p-6">
                <h3 class="text-2xl font-bold text-[#0057B8] mb-2">UNICEF</h3>
                <p class="text-gray-600">Захист прав та інтересів дітей.</p>
            </div>
            <div class="p-6">
                <h3 class="text-2xl font-bold text-[#0057B8] mb-2">Red Cross</h3>
                <p class="text-gray-600">Гуманітарна допомога постраждалим.</p>
            </div>
        </div>
    </section>
    """
    
    intl_html_en = """
    <section class="relative py-20 overflow-hidden">
        <div class="relative z-10 max-w-4xl mx-auto text-center px-4">
            <div class="inline-block px-4 py-1 rounded-full bg-yellow-100 text-yellow-800 font-bold text-sm mb-4 uppercase tracking-wider">Cooperation</div>
            <h1 class="text-4xl md:text-6xl font-heading font-bold text-[#212529] mb-6">International Partners</h1>
            <p class="text-xl text-gray-600 max-w-2xl mx-auto">We unite efforts with global organizations to implement large-scale humanitarian projects.</p>
        </div>
    </section>
    <section class="py-12 max-w-6xl mx-auto px-4 bg-gray-50 rounded-3xl">
        <div class="grid md:grid-cols-3 gap-8 text-center">
            <div class="p-6">
                <h3 class="text-2xl font-bold text-[#0057B8] mb-2">USAID</h3>
                <p class="text-gray-600">Supporting democracy and economic development.</p>
            </div>
            <div class="p-6">
                <h3 class="text-2xl font-bold text-[#0057B8] mb-2">UNICEF</h3>
                <p class="text-gray-600">Protecting children's rights and interests.</p>
            </div>
            <div class="p-6">
                <h3 class="text-2xl font-bold text-[#0057B8] mb-2">Red Cross</h3>
                <p class="text-gray-600">Humanitarian aid for victims.</p>
            </div>
        </div>
    </section>
    """
    intl_page.content_uk = intl_html_uk
    intl_page.content_en = intl_html_en
    intl_page.save()
    print("International Page updated.")

    # --- Volunteering Page ---
    vol_page, created = VolunteeringPage.objects.get_or_create(id=1)
    vol_page.title_uk = "Волонтерство"
    vol_page.title_en = "Volunteering"
    
    vol_html_uk = """
    <section class="relative py-24 bg-[#FFD700] rounded-3xl my-8 mx-4 md:mx-0 overflow-hidden text-[#212529]">
        <div class="relative z-10 max-w-5xl mx-auto text-center px-4">
            <h1 class="text-4xl md:text-6xl font-heading font-bold mb-6 leading-tight">Твоя суперсила — небайдужість</h1>
            <p class="text-xl font-medium max-w-3xl mx-auto leading-relaxed mb-8">Кожна година твого часу може змінити чиєсь життя. Приєднуйся до команди, яка творить дива своїми руками.</p>
            <a href="#join-form" class="inline-block px-8 py-4 bg-[#212529] text-white font-bold rounded-xl hover:bg-gray-800 transition shadow-lg transform hover:scale-105">Заповнити анкету</a>
        </div>
    </section>
    <section class="py-16 max-w-6xl mx-auto px-4">
        <div class="grid md:grid-cols-3 gap-8">
            <div class="bg-white p-8 rounded-2xl shadow-sm border border-gray-100">
                <h3 class="text-xl font-bold text-[#212529] mb-3">Логістика</h3>
                <p class="text-gray-600">Допомога у сортуванні та доставці гуманітарних вантажів.</p>
            </div>
            <div class="bg-white p-8 rounded-2xl shadow-sm border border-gray-100">
                <h3 class="text-xl font-bold text-[#212529] mb-3">IT та Медіа</h3>
                <p class="text-gray-600">Розробка, дизайн, ведення соцмереж та фотозйомка.</p>
            </div>
            <div class="bg-white p-8 rounded-2xl shadow-sm border border-gray-100">
                <h3 class="text-xl font-bold text-[#212529] mb-3">Івенти</h3>
                <p class="text-gray-600">Організація благодійних заходів та акцій.</p>
            </div>
        </div>
    </section>
    """
    
    vol_html_en = """
    <section class="relative py-24 bg-[#FFD700] rounded-3xl my-8 mx-4 md:mx-0 overflow-hidden text-[#212529]">
        <div class="relative z-10 max-w-5xl mx-auto text-center px-4">
            <h1 class="text-4xl md:text-6xl font-heading font-bold mb-6 leading-tight">Your Superpower is Caring</h1>
            <p class="text-xl font-medium max-w-3xl mx-auto leading-relaxed mb-8">Every hour of your time can change someone's life. Join the team that creates miracles with their own hands.</p>
            <a href="#join-form" class="inline-block px-8 py-4 bg-[#212529] text-white font-bold rounded-xl hover:bg-gray-800 transition shadow-lg transform hover:scale-105">Fill out the form</a>
        </div>
    </section>
    <section class="py-16 max-w-6xl mx-auto px-4">
        <div class="grid md:grid-cols-3 gap-8">
            <div class="bg-white p-8 rounded-2xl shadow-sm border border-gray-100">
                <h3 class="text-xl font-bold text-[#212529] mb-3">Logistics</h3>
                <p class="text-gray-600">Assistance in sorting and delivering humanitarian cargo.</p>
            </div>
            <div class="bg-white p-8 rounded-2xl shadow-sm border border-gray-100">
                <h3 class="text-xl font-bold text-[#212529] mb-3">IT & Media</h3>
                <p class="text-gray-600">Development, design, social media management, and photography.</p>
            </div>
            <div class="bg-white p-8 rounded-2xl shadow-sm border border-gray-100">
                <h3 class="text-xl font-bold text-[#212529] mb-3">Events</h3>
                <p class="text-gray-600">Organization of charity events and campaigns.</p>
            </div>
        </div>
    </section>
    """
    vol_page.content_uk = vol_html_uk
    vol_page.content_en = vol_html_en
    vol_page.save()
    print("Volunteering Page updated.")

    # --- Projects Page ---
    proj_page, created = ProjectsPage.objects.get_or_create(id=1)
    proj_page.title_uk = "Наші Проєкти"
    proj_page.title_en = "Our Projects"
    
    proj_html_uk = """
    <section class="relative py-20 overflow-hidden">
        <div class="relative z-10 max-w-4xl mx-auto text-center px-4">
            <div class="inline-block px-4 py-1 rounded-full bg-green-100 text-green-700 font-bold text-sm mb-4 uppercase tracking-wider">Реальні дії</div>
            <h1 class="text-4xl md:text-6xl font-heading font-bold text-[#212529] mb-6">Наші Проєкти</h1>
            <p class="text-xl text-gray-600 max-w-2xl mx-auto">Від ідеї до результату. Ми втілюємо в життя ініціативи, що змінюють світ навколо нас.</p>
        </div>
    </section>
    <section class="py-16 max-w-7xl mx-auto px-4">
        <div class="grid md:grid-cols-3 gap-8">
            <div class="bg-white rounded-2xl overflow-hidden shadow-lg hover:shadow-xl transition flex flex-col h-full">
                <div class="h-48 bg-gray-200 flex items-center justify-center text-gray-400">Фото проєкту</div>
                <div class="p-8 flex flex-col flex-grow">
                    <h3 class="text-2xl font-bold text-[#212529] mb-4">Допомога дітям</h3>
                    <p class="text-gray-600 mb-6 flex-grow">Забезпечення дитячих будинків необхідними речами та організація свят.</p>
                    <span class="text-[#0057B8] font-bold">Детальніше &rarr;</span>
                </div>
            </div>
            <div class="bg-white rounded-2xl overflow-hidden shadow-lg hover:shadow-xl transition flex flex-col h-full">
                <div class="h-48 bg-gray-200 flex items-center justify-center text-gray-400">Фото проєкту</div>
                <div class="p-8 flex flex-col flex-grow">
                    <h3 class="text-2xl font-bold text-[#212529] mb-4">Відбудова</h3>
                    <p class="text-gray-600 mb-6 flex-grow">Допомога у відновленні пошкоджених будинків у деокупованих регіонах.</p>
                    <span class="text-[#0057B8] font-bold">Детальніше &rarr;</span>
                </div>
            </div>
            <div class="bg-white rounded-2xl overflow-hidden shadow-lg hover:shadow-xl transition flex flex-col h-full">
                <div class="h-48 bg-gray-200 flex items-center justify-center text-gray-400">Фото проєкту</div>
                <div class="p-8 flex flex-col flex-grow">
                    <h3 class="text-2xl font-bold text-[#212529] mb-4">Медицина</h3>
                    <p class="text-gray-600 mb-6 flex-grow">Закупівля сучасного обладнання для лікарень.</p>
                    <span class="text-[#0057B8] font-bold">Детальніше &rarr;</span>
                </div>
            </div>
        </div>
    </section>
    """
    
    proj_html_en = """
    <section class="relative py-20 overflow-hidden">
        <div class="relative z-10 max-w-4xl mx-auto text-center px-4">
            <div class="inline-block px-4 py-1 rounded-full bg-green-100 text-green-700 font-bold text-sm mb-4 uppercase tracking-wider">Real Actions</div>
            <h1 class="text-4xl md:text-6xl font-heading font-bold text-[#212529] mb-6">Our Projects</h1>
            <p class="text-xl text-gray-600 max-w-2xl mx-auto">From idea to result. We bring to life initiatives that change the world around us.</p>
        </div>
    </section>
    <section class="py-16 max-w-7xl mx-auto px-4">
        <div class="grid md:grid-cols-3 gap-8">
            <div class="bg-white rounded-2xl overflow-hidden shadow-lg hover:shadow-xl transition flex flex-col h-full">
                <div class="h-48 bg-gray-200 flex items-center justify-center text-gray-400">Project Photo</div>
                <div class="p-8 flex flex-col flex-grow">
                    <h3 class="text-2xl font-bold text-[#212529] mb-4">Help for Children</h3>
                    <p class="text-gray-600 mb-6 flex-grow">Providing orphanages with necessary items and organizing holidays.</p>
                    <span class="text-[#0057B8] font-bold">Read more &rarr;</span>
                </div>
            </div>
            <div class="bg-white rounded-2xl overflow-hidden shadow-lg hover:shadow-xl transition flex flex-col h-full">
                <div class="h-48 bg-gray-200 flex items-center justify-center text-gray-400">Project Photo</div>
                <div class="p-8 flex flex-col flex-grow">
                    <h3 class="text-2xl font-bold text-[#212529] mb-4">Reconstruction</h3>
                    <p class="text-gray-600 mb-6 flex-grow">Assistance in restoring damaged houses in de-occupied regions.</p>
                    <span class="text-[#0057B8] font-bold">Read more &rarr;</span>
                </div>
            </div>
            <div class="bg-white rounded-2xl overflow-hidden shadow-lg hover:shadow-xl transition flex flex-col h-full">
                <div class="h-48 bg-gray-200 flex items-center justify-center text-gray-400">Project Photo</div>
                <div class="p-8 flex flex-col flex-grow">
                    <h3 class="text-2xl font-bold text-[#212529] mb-4">Medicine</h3>
                    <p class="text-gray-600 mb-6 flex-grow">Purchase of modern equipment for hospitals.</p>
                    <span class="text-[#0057B8] font-bold">Read more &rarr;</span>
                </div>
            </div>
        </div>
    </section>
    """
    proj_page.content_uk = proj_html_uk
    proj_page.content_en = proj_html_en
    proj_page.save()
    print("Projects Page updated.")

if __name__ == '__main__':
    populate()
