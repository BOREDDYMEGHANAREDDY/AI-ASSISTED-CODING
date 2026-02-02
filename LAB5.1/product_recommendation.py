"""
Explainable Product Recommendation System
Provides transparent, understandable product recommendations with clear reasoning
"""

from dataclasses import dataclass
from typing import List, Dict, Tuple
from enum import Enum


# ============================================================================
# DATA STRUCTURES
# ============================================================================

class Category(Enum):
    """Product categories."""
    ELECTRONICS = "Electronics"
    BOOKS = "Books"
    CLOTHING = "Clothing"
    HOME = "Home & Kitchen"
    SPORTS = "Sports & Outdoors"
    BEAUTY = "Beauty & Personal Care"


@dataclass
class Product:
    """Represents a product with its attributes."""
    product_id: int
    name: str
    category: Category
    price: float
    rating: float
    description: str
    features: List[str]
    
    def __str__(self):
        return f"{self.name} (${self.price:.2f}) - Rating: {self.rating}/5"


@dataclass
class UserPreference:
    """Represents user's preferences and purchase history."""
    user_id: int
    name: str
    budget_min: float
    budget_max: float
    preferred_categories: List[Category]
    preferred_features: List[str]
    purchase_history: List[int]  # Product IDs
    minimum_rating: float
    
    def __str__(self):
        return (f"User: {self.name}\n"
                f"  Budget: ${self.budget_min:.2f} - ${self.budget_max:.2f}\n"
                f"  Preferred Categories: {', '.join([c.value for c in self.preferred_categories])}\n"
                f"  Minimum Rating: {self.minimum_rating}/5")


@dataclass
class Recommendation:
    """Represents a single recommendation with explanation."""
    product: Product
    match_score: float  # 0-100%
    reasons: List[str]  # Why this product is recommended
    matching_features: List[str]  # User features this product has
    
    def __str__(self):
        reasons_text = "\n    ".join(self.reasons)
        features_text = ", ".join(self.matching_features)
        return (f"{self.product.name}\n"
                f"  Match Score: {self.match_score:.1f}%\n"
                f"  Price: ${self.product.price:.2f}\n"
                f"  Rating: {self.product.rating}/5\n"
                f"  Matching Features: {features_text}\n"
                f"  Why Recommended:\n"
                f"    {reasons_text}")


# ============================================================================
# PRODUCT DATABASE
# ============================================================================

class ProductDatabase:
    """Manages the product catalog."""
    
    def __init__(self):
        """Initialize with sample products."""
        self.products = self._create_sample_products()
    
    def _create_sample_products(self) -> List[Product]:
        """Create a sample product database."""
        return [
            # Electronics
            Product(
                product_id=1,
                name="Wireless Headphones Pro",
                category=Category.ELECTRONICS,
                price=129.99,
                rating=4.7,
                description="Premium noise-canceling headphones",
                features=["noise-canceling", "wireless", "long-battery", "comfortable", "high-quality-sound"]
            ),
            Product(
                product_id=2,
                name="USB-C Fast Charger",
                category=Category.ELECTRONICS,
                price=39.99,
                rating=4.3,
                description="High-speed charging adapter",
                features=["fast-charging", "compact", "durable", "universal-compatibility"]
            ),
            Product(
                product_id=3,
                name="Smart Watch Elite",
                category=Category.ELECTRONICS,
                price=299.99,
                rating=4.5,
                description="Advanced fitness and health tracking",
                features=["fitness-tracking", "heart-rate-monitor", "water-resistant", "long-battery"]
            ),
            
            # Books
            Product(
                product_id=4,
                name="Python Programming Mastery",
                category=Category.BOOKS,
                price=49.99,
                rating=4.8,
                description="Comprehensive Python learning guide",
                features=["programming", "beginner-friendly", "practical-examples", "well-structured"]
            ),
            Product(
                product_id=5,
                name="Data Science Fundamentals",
                category=Category.BOOKS,
                price=59.99,
                rating=4.6,
                description="Learn data science from scratch",
                features=["data-science", "machine-learning", "practical-projects", "beginner-friendly"]
            ),
            Product(
                product_id=6,
                name="The Midnight Library",
                category=Category.BOOKS,
                price=16.99,
                rating=4.4,
                description="Bestselling fiction novel",
                features=["fiction", "inspirational", "thought-provoking", "easy-read"]
            ),
            
            # Clothing
            Product(
                product_id=7,
                name="Athletic Running Shoes",
                category=Category.CLOTHING,
                price=89.99,
                rating=4.6,
                description="Lightweight professional running shoes",
                features=["comfortable", "breathable", "good-support", "durable", "lightweight"]
            ),
            Product(
                product_id=8,
                name="Winter Jacket Pro",
                category=Category.CLOTHING,
                price=159.99,
                rating=4.5,
                description="Insulated waterproof jacket",
                features=["warm", "waterproof", "lightweight", "stylish", "durable"]
            ),
            Product(
                product_id=9,
                name="Casual Cotton T-Shirt",
                category=Category.CLOTHING,
                price=19.99,
                rating=4.2,
                description="Comfortable everyday t-shirt",
                features=["comfortable", "breathable", "soft", "affordable"]
            ),
            
            # Home & Kitchen
            Product(
                product_id=10,
                name="Stainless Steel Blender",
                category=Category.HOME,
                price=79.99,
                rating=4.7,
                description="Powerful multi-function blender",
                features=["powerful", "durable", "easy-cleanup", "quiet-operation", "versatile"]
            ),
            Product(
                product_id=11,
                name="Coffee Maker Deluxe",
                category=Category.HOME,
                price=99.99,
                rating=4.4,
                description="Programmable coffee brewing system",
                features=["programmable", "timer", "durable", "easy-to-use"]
            ),
            Product(
                product_id=12,
                name="Bamboo Cutting Board Set",
                category=Category.HOME,
                price=24.99,
                rating=4.5,
                description="Eco-friendly cutting boards",
                features=["eco-friendly", "durable", "easy-cleanup", "affordable"]
            ),
            
            # Sports & Outdoors
            Product(
                product_id=13,
                name="Professional Yoga Mat",
                category=Category.SPORTS,
                price=34.99,
                rating=4.6,
                description="Non-slip exercise and yoga mat",
                features=["non-slip", "comfortable", "eco-friendly", "portable"]
            ),
            Product(
                product_id=14,
                name="Mountain Bike 21-Speed",
                category=Category.SPORTS,
                price=349.99,
                rating=4.7,
                description="Durable off-road mountain bike",
                features=["durable", "fast", "all-terrain", "good-suspension"]
            ),
            Product(
                product_id=15,
                name="Portable Water Bottle",
                category=Category.SPORTS,
                price=29.99,
                rating=4.8,
                description="Lightweight insulated water bottle",
                features=["lightweight", "durable", "keeps-cold", "leakproof"]
            ),
            
            # Beauty & Personal Care
            Product(
                product_id=16,
                name="Organic Skincare Set",
                category=Category.BEAUTY,
                price=69.99,
                rating=4.5,
                description="Natural ingredients skincare kit",
                features=["organic", "natural-ingredients", "gentle", "effective"]
            ),
            Product(
                product_id=17,
                name="Electric Toothbrush Pro",
                category=Category.BEAUTY,
                price=59.99,
                rating=4.6,
                description="Advanced oral care technology",
                features=["effective", "gentle", "durable", "smart-timer"]
            ),
            Product(
                product_id=18,
                name="Premium Hair Dryer",
                category=Category.BEAUTY,
                price=79.99,
                rating=4.4,
                description="High-speed ionic hair dryer",
                features=["fast-drying", "ionic-technology", "multiple-settings", "quiet"]
            ),
        ]
    
    def get_product(self, product_id: int) -> Product:
        """Get a product by ID."""
        for product in self.products:
            if product.product_id == product_id:
                return product
        return None
    
    def get_all_products(self) -> List[Product]:
        """Get all products."""
        return self.products
    
    def get_products_by_category(self, category: Category) -> List[Product]:
        """Get products in a specific category."""
        return [p for p in self.products if p.category == category]


# ============================================================================
# RECOMMENDATION ENGINE
# ============================================================================

class RecommendationEngine:
    """Generates explainable product recommendations."""
    
    def __init__(self, database: ProductDatabase):
        """Initialize the recommendation engine."""
        self.database = database
    
    def recommend_products(
        self,
        user: UserPreference,
        num_recommendations: int = 5
    ) -> List[Recommendation]:
        """
        Generate product recommendations with explanations.
        
        Args:
            user: User preferences and constraints
            num_recommendations: Number of products to recommend
            
        Returns:
            List of recommendations sorted by match score (highest first)
        """
        
        recommendations = []
        
        # Get all products excluding already purchased
        available_products = [
            p for p in self.database.get_all_products()
            if p.product_id not in user.purchase_history
        ]
        
        # Calculate match score for each product
        for product in available_products:
            match_score, reasons, matching_features = self._calculate_match_score(
                product, user
            )
            
            # Only include products that meet minimum criteria
            if match_score > 0:
                recommendation = Recommendation(
                    product=product,
                    match_score=match_score,
                    reasons=reasons,
                    matching_features=matching_features
                )
                recommendations.append(recommendation)
        
        # Sort by match score (highest first)
        recommendations.sort(key=lambda r: r.match_score, reverse=True)
        
        # Return top N recommendations
        return recommendations[:num_recommendations]
    
    def _calculate_match_score(
        self,
        product: Product,
        user: UserPreference
    ) -> Tuple[float, List[str], List[str]]:
        """
        Calculate how well a product matches user preferences.
        
        Args:
            product: Product to evaluate
            user: User preferences
            
        Returns:
            Tuple of (match_score, reasons, matching_features)
        """
        
        score = 0.0
        max_score = 0.0
        reasons = []
        matching_features = []
        
        # ===== CATEGORY MATCHING (20 points max) =====
        max_score += 20
        if product.category in user.preferred_categories:
            score += 20
            reasons.append(f"Matches preferred category: {product.category.value}")
        else:
            reasons.append(f"Category: {product.category.value} (not in preferred list)")
        
        # ===== BUDGET MATCHING (20 points max) =====
        max_score += 20
        if user.budget_min <= product.price <= user.budget_max:
            score += 20
            reasons.append(f"Within budget range (${user.budget_min:.2f}-${user.budget_max:.2f})")
        else:
            reasons.append(f"Price ${product.price:.2f} is outside budget range")
            return 0, reasons, matching_features  # Skip if outside budget
        
        # ===== RATING MATCHING (15 points max) =====
        max_score += 15
        if product.rating >= user.minimum_rating:
            # Award points based on how much above minimum
            rating_bonus = (product.rating - user.minimum_rating) / (5 - user.minimum_rating)
            score += 15 * rating_bonus
            reasons.append(f"Good rating: {product.rating}/5 (minimum: {user.minimum_rating}/5)")
        else:
            return 0, reasons, matching_features  # Skip if below minimum rating
        
        # ===== FEATURE MATCHING (45 points max) =====
        max_score += 45
        feature_match_count = 0
        for feature in product.features:
            if feature in user.preferred_features:
                feature_match_count += 1
                matching_features.append(feature)
        
        if feature_match_count > 0:
            feature_score = (feature_match_count / max(len(user.preferred_features), 1)) * 45
            score += feature_score
            features_str = ", ".join(matching_features)
            reasons.append(f"Has {feature_match_count} preferred features: {features_str}")
        else:
            reasons.append("No preferred features found in this product")
        
        # ===== NORMALIZE TO PERCENTAGE =====
        if max_score > 0:
            match_percentage = (score / max_score) * 100
        else:
            match_percentage = 0
        
        return match_percentage, reasons, matching_features
    
    def explain_recommendation(self, recommendation: Recommendation) -> str:
        """
        Generate a detailed explanation for a recommendation.
        
        Args:
            recommendation: The recommendation to explain
            
        Returns:
            Formatted explanation text
        """
        explanation = f"""
╔════════════════════════════════════════════════════════════════╗
║  PRODUCT RECOMMENDATION: {recommendation.product.name[:55]}
╚════════════════════════════════════════════════════════════════╝

Match Score: {recommendation.match_score:.1f}%
{"█" * int(recommendation.match_score / 5)}{"░" * (20 - int(recommendation.match_score / 5))}

Product Details:
  • Price: ${recommendation.product.price:.2f}
  • Rating: {recommendation.product.rating}/5 ⭐
  • Category: {recommendation.product.category.value}
  • Description: {recommendation.product.description}

Why We Recommend This:
"""
        for i, reason in enumerate(recommendation.reasons, 1):
            explanation += f"  {i}. {reason}\n"
        
        explanation += f"""
All Product Features:
  • {', '.join(recommendation.product.features)}

Your Matching Features:
  • {', '.join(recommendation.matching_features) if recommendation.matching_features else 'None'}
"""
        return explanation


# ============================================================================
# SAMPLE DATA & TESTING
# ============================================================================

def create_sample_user_1() -> UserPreference:
    """Tech-savvy user who likes gadgets."""
    return UserPreference(
        user_id=1,
        name="Alice Johnson",
        budget_min=50.0,
        budget_max=300.0,
        preferred_categories=[
            Category.ELECTRONICS,
            Category.BOOKS,
            Category.SPORTS
        ],
        preferred_features=[
            "wireless",
            "noise-canceling",
            "long-battery",
            "fast-charging",
            "programming",
            "portable"
        ],
        purchase_history=[2, 5],  # Already bought USB charger and Data Science book
        minimum_rating=4.3
    )


def create_sample_user_2() -> UserPreference:
    """Health and fitness focused user."""
    return UserPreference(
        user_id=2,
        name="Bob Smith",
        budget_min=20.0,
        budget_max=400.0,
        preferred_categories=[
            Category.SPORTS,
            Category.CLOTHING,
            Category.BEAUTY,
            Category.HOME
        ],
        preferred_features=[
            "comfortable",
            "durable",
            "fitness-tracking",
            "eco-friendly",
            "lightweight",
            "water-resistant"
        ],
        purchase_history=[13],  # Already bought yoga mat
        minimum_rating=4.4
    )


def create_sample_user_3() -> UserPreference:
    """Budget-conscious home and book lover."""
    return UserPreference(
        user_id=3,
        name="Carol Davis",
        budget_min=10.0,
        budget_max=100.0,
        preferred_categories=[
            Category.BOOKS,
            Category.HOME,
            Category.CLOTHING
        ],
        preferred_features=[
            "affordable",
            "durable",
            "easy-cleanup",
            "practical-examples",
            "eco-friendly",
            "beginner-friendly"
        ],
        purchase_history=[9],  # Already bought t-shirt
        minimum_rating=4.2
    )


# ============================================================================
# MAIN PROGRAM
# ============================================================================

def main():
    """Run the recommendation system."""
    
    print("="*70)
    print("EXPLAINABLE PRODUCT RECOMMENDATION SYSTEM")
    print("="*70)
    
    # Initialize database and engine
    database = ProductDatabase()
    engine = RecommendationEngine(database)
    
    # Create sample users
    users = [
        create_sample_user_1(),
        create_sample_user_2(),
        create_sample_user_3()
    ]
    
    # Generate recommendations for each user
    for user in users:
        print(f"\n\n{'='*70}")
        print(f"RECOMMENDATIONS FOR: {user.name}")
        print(f"{'='*70}")
        print(user)
        
        # Get recommendations
        recommendations = engine.recommend_products(user, num_recommendations=5)
        
        print(f"\n\nTop {len(recommendations)} Recommendations:")
        print("-" * 70)
        
        for rank, recommendation in enumerate(recommendations, 1):
            print(f"\n#{rank}")
            print(engine.explain_recommendation(recommendation))
            print("-" * 70)
    
    # Interactive mode
    print("\n\n" + "="*70)
    print("INTERACTIVE RECOMMENDATION MODE")
    print("="*70)
    
    while True:
        print("\nOptions:")
        print("1. Get recommendations for a sample user")
        print("2. Create custom user and get recommendations")
        print("3. View all products")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == '1':
            print("\nSample Users:")
            print("1. Alice Johnson (Tech enthusiast)")
            print("2. Bob Smith (Fitness focused)")
            print("3. Carol Davis (Budget conscious)")
            
            user_choice = input("Select user (1-3): ").strip()
            if user_choice in ['1', '2', '3']:
                sample_users = [create_sample_user_1(), create_sample_user_2(), create_sample_user_3()]
                user = sample_users[int(user_choice) - 1]
                
                recommendations = engine.recommend_products(user, num_recommendations=5)
                print(f"\n\nRecommendations for {user.name}:")
                print("="*70)
                
                for rank, rec in enumerate(recommendations, 1):
                    print(f"\n#{rank}")
                    print(engine.explain_recommendation(rec))
        
        elif choice == '2':
            print("\nCreating custom user profile...")
            print("\nAvailable categories:")
            for i, cat in enumerate(Category, 1):
                print(f"{i}. {cat.value}")
            
            print("\nThis would require detailed input. Using sample user instead.")
            user = create_sample_user_1()
            recommendations = engine.recommend_products(user, num_recommendations=5)
            
            print(f"\nRecommendations:")
            for rank, rec in enumerate(recommendations, 1):
                print(f"\n#{rank}")
                print(engine.explain_recommendation(rec))
        
        elif choice == '3':
            print("\n\nAll Products in Catalog:")
            print("="*70)
            for product in database.get_all_products():
                print(f"\n[{product.product_id:2d}] {product.name}")
                print(f"      Category: {product.category.value}")
                print(f"      Price: ${product.price:.2f}")
                print(f"      Rating: {product.rating}/5")
                print(f"      Features: {', '.join(product.features)}")
        
        elif choice == '4':
            print("\nThank you for using the Recommendation System!")
            break
        
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
