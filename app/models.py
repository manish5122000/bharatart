from django.db import models
from django.contrib.auth.models import User
from .utils import generate_ref_code

# Create your models here.
COUNTRY_CHOICES = (
    ('Indian', 'Indian'),
    ('Other', 'Other')
)

CITY_CHOICE = (
    ('Agra', 'Agra'),
    ('Aligarh', 'Aligarh'),
    ('Allahabad', 'Allahabad'),
    ('Ambedkar Nagar', 'Ambedkar Nagar'),
    ('Amethi', 'Amethi'),
    ('Amroha', 'Amroha'),
    ('Auraiya', 'Auraiya'),
    ('Azamgarh', 'Azamgarh'),
    ('Baghpat', 'Baghpat'),
    ('Bahraich', 'Bahraich'),
    ('Ballia', 'Ballia'),
    ('Balrampur', 'Balrampur'),
    ('Banda', 'Banda'),
    ('Barabanki', 'Barabanki'),
    ('Bareilly', 'Bareilly'),
    ('Basti', 'Basti'),
    ('Bhadohi', 'Bhadohi'),
    ('Bijnor', 'Bijnor'),
    ('Budaun', 'Budaun'),
    ('Bulandshahr', 'Bulandshahr'),
    ('Chandauli', 'Chitrakoot'),
    ('Deoria', 'Deoria'),
    ('Etah', 'Etah'),
    ('Etawah', 'Etawah'),
    ('Faizabad', 'Faizabad'),
    ('Farrukhabad', 'Farrukhabad'),
    ('Fatehpur', 'Fatehpur'),
    ('Firozabad', 'Firozabad'),
    ('Gautam Buddha Nagar', 'Gautam Buddha Nagar'),
    ('Ghaziabad', 'Ghaziabad'),
    ('Ghazipur', 'Ghazipur'),
    ('Gonda', 'Gonda'),
    ('Gorakhpur', 'Gorakhpur'),
    ('Hamirpur', 'Hamirpur'),
    ('Hapur', 'Hapur'),
    ('Hardoi', 'Hardoi'),
    ('Hathras', 'Hathras'),
    ('Jalaun', 'Jalaun'),
    ('Jaunpur', 'Jaunpur'),
    ('Jhansi', 'Jhansi'),
    ('Kannauj', 'Kannauj'),
    ('Kanpur Dehat', 'Kanpur Dehat'),
    ('Kanpur Nagar', 'Kanpur Nagar'),
    ('Kanshiram Nagar', 'Kanshiram Nagar'),
    ('Kaushambi', 'Kaushambi'),
    ('Kushinagar', 'Kushinagar'),
    ('Lakhimpur ', 'Lakhimpur '),
    ('Lalitpur', 'Lalitpur'),
    ('Lucknow', 'Lucknow'),
    ('Maharajganj', 'Maharajganj'),
    ('Mahoba', 'Mahoba'),
    ('Mainpuri', 'Mainpuri'),
    ('Mathura', 'Mathura'),
    ('Mau', 'Mau'),
    ('Meerut', 'Meerut'),
    ('Mirzapur', 'Mirzapur'),
    ('Moradabad', 'Moradabad'),
    ('Muzaffarnagar', 'Muzaffarnagar'),
    ('Pilibhit', 'Pilibhit'),
    ('Pratapgarh', 'Pratapgarh'),
    ('RaeBareli', 'RaeBareli'),
    ('Rampur', 'Rampur'),
    ('Saharanpur', 'Saharanpur'),
    ('Sambhal ', 'Sambhal '),
    ('Sant Kabir Nagar', 'Sant Kabir Nagar'),
    ('Shahjahanpur', 'Shahjahanpur'),
    ('Shamali ', 'Shamali '),
    ('Shravasti', 'Shravasti'),
    ('Siddharth Nagar', 'Siddharth Nagar'),
    ('Sitapur', 'Sitapur'),
    ('Sonbhadra', 'Sonbhadra'),
    ('Sultanpur', 'Sultanpur'),
    ('Unnao', 'Unnao'),
    ('Varanasi', 'Varanasi')
               
)

class Support_User_Sponser_detail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, blank=True)
    city = models.CharField(choices=CITY_CHOICE, max_length=50, blank=True)
    sponser_id = models.CharField(max_length=6, blank=True, primary_key=True)
    mobile_no = models.PositiveBigIntegerField(default='1234567890')
    # recommended_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ref_by', blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    def __str__(self) -> str:
        return f"{self.user.username}-{self.sponser_id}"

    def get_recommended_profiles(self):
        pass

    def save(self, *args, **kwargs):
        if self.sponser_id == "":
            sponser_id = generate_ref_code()
            self.sponser_id = sponser_id
        super().save(*args, **kwargs)

    
