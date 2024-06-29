import random
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from myapp.models import Recipe, Category

text = ('dolor sit amet consectetur adipisicing elit Hic adipisci odio '
        'deleniti fugiat facilis ducimus ipsa a saepe earum aut sapiente '
        'nemo nihil incidunt numquam Dolorem obcaecati sequi voluptates '
        'aliquid harum excepturi quod nihil consequuntur nulla Delectus eaque '
        'corrupti minima commodi repellat esse eveniet vel rem necessitatibus '
        'ipsam molestiae accusantium beatae Porro numquam corrupti enim '
        'dolorem omnis quibusdam itaque odio ipsa minima expedita quo aut '
        'laudantium at ipsam commodi doloremque quasi illo accusantium qui '
        'Praesentium illum porro excepturi blanditiis iure distinctio omnis '
        'perferendis maxime placeat exercitationem quisquam labore aperiam '
        'nostrum amet impedit veniam laudantium aut consectetur commodi '
        'maiores harum facere sunt Consectetur soluta atque sit voluptas '
        'aliquid iure deleniti quam voluptatem repellat id esse nobis '
        'quisquam Culpa quo animi soluta illo labore veritatis cum quae ut '
        'placeat tempore expedita magnam explicabo pariatur fuga voluptate '
        'officiis error laborum sint enim natus a Quasi reiciendis eligendi '
        'necessitatibus quis ratione eos sapiente rem fuga nam neque '
        'blanditiis expedita accusamus porro dicta libero in esse laborum '
        'quidem aut autem placeat praesentium Veniam laboriosam saepe '
        'voluptatibus pariatur unde laudantium illum eveniet facilis voluptas '
        'similique soluta quaerat dignissimos officia distinctio')
text_list = text.split(' ')
recipe_list = [random.choice(text_list) for _ in range(20)]
recipe_text = f'Lorem ipsum {" ".join(recipe_list)}.'


class Command(BaseCommand):
    help = 'Generate recipe'

    def handle(self, *args, **kwargs):
        recipe = Recipe(
            title=f'Селедка под шубой',
            description=recipe_text,
            ingredients=recipe_text,
            steps=recipe_text,
            image='recipes/bunny_maam_soft_pastel_colors_adorable_anthropomorphic_tall_a_599c4d98-320c-4c39_R9QdR1d.png',
            author=User.objects.filter(pk=1).first(),
        )
        recipe.save()

        category = Category.objects.get(pk=2)
        recipe.categories.add(category)

        self.stdout.write(
            f'Добавлен новый рецепт')
