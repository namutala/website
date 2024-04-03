# from django.shortcuts import render, redirect
# from .models import Item, Review
# from .forms import ReviewForm

# from django.shortcuts import render, redirect
# from .models import Item, Review
# from .forms import ReviewForm

# def item_detail(request, item_id):
#     item = Item.objects.get(pk=item_id)
#     reviews = item.reviews.all()
#     form = ReviewForm()
#     return render(request, 'item_detail.html', {'item': item, 'reviews': reviews, 'form': form})

# def add_review(request, item_id):
#     if request.method == 'POST':
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             item = Item.objects.get(pk=item_id)
#             Review.objects.create(
#                 item=item,
#                 user=request.user,
#                 rating=form.cleaned_data['rating'],
#                 comment=form.cleaned_data['comment']
#             )
#             return redirect('item_detail', item_id=item_id)
#     else:
#         form = ReviewForm()
#     return render(request, 'add_review.html', {'form': form})
