import axios from 'axios';
import type { NextApiRequest, NextApiResponse } from 'next';

const processUrl = async (req: NextApiRequest, res: NextApiResponse) => {
    if (req.method === 'POST') {
        const { url } = req.body;
        try {
            const response = await axios.post(`${process.env.API_URL}/process-url`, { url });
            return res.status(200).json(response.data);
        } catch (error) {
            console.error(error);  // Utilize error variable
            return res.status(500).json({ message: "Internal server error" });
        }
    } else {
        res.setHeader('Allow', ['POST']);
        return res.status(405).end(`Method ${req.method} Not Allowed`);
    }
};

export default processUrl;
