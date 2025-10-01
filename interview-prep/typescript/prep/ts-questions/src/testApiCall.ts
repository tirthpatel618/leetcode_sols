
interface UserRating {
    average_rating: number;
    votes: number;
}

interface FoodOutlet {
    city: string;
    name: string;
    estimated_cost: number;
    user_rating: UserRating;
    id: number;
}

interface ApiResponse {
    page: number;
    per_page: number;
    total: number;
    total_pages: number;
    data: FoodOutlet[];
}


async function getRelevantFoodOutlets(city: string, maxCost: number): Promise<string[]> {
    const result : string[] = []
    let page = 1;

    while (true) {
        try {
            const url = `https://jsonmock.hackerrank.com/api/food_outlets?city=${city}&page=${page}`;
            const response = await fetch(url);

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }


            const data: ApiResponse = await response.json();

            for (const outlet of data.data) {
                if (outlet.estimated_cost <= maxCost) {
                    result.push(outlet.name);
                }
            }

            if (data.page === data.total_pages) {
                break;
            }
            
            page++;
        }  catch (error) {
            console.error(error);
            throw error;
        }
    } 
    return result;
}

async function main(): Promise<void> {
    try {
        const city = "Denver";
        const maxCost = 50;
        
        console.log(`Fetching food outlets in ${city} with max cost ${maxCost}...`);
        const outlets = await getRelevantFoodOutlets(city, maxCost);
        
        console.log('Results:');
        outlets.forEach((outlet, index) => {
            console.log(`${index + 1}. ${outlet}`);
        });
        
        console.log(`\nTotal outlets found: ${outlets.length}`);
    } catch (error) {
        console.error('Error in main function:', error);
    }
}

main();